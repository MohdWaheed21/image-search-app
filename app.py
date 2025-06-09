import os
import json
import requests
from flask import Flask, render_template, request, jsonify, url_for

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
EMBEDDINGS_FILE = 'embeddings.json'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load existing embeddings or create empty dict
def load_embeddings():
    if os.path.exists(EMBEDDINGS_FILE):
        with open(EMBEDDINGS_FILE, 'r') as f:
            try:
                data = json.load(f)
                # Ensure it is a dict, else reset
                if isinstance(data, dict):
                    return data
                else:
                    print("Warning: embeddings.json is not a dict. Resetting to empty dict.")
                    return {}
            except json.JSONDecodeError:
                print("Warning: embeddings.json is invalid JSON. Resetting to empty dict.")
                return {}
    else:
        return {}

embeddings = load_embeddings()

def save_embeddings():
    with open(EMBEDDINGS_FILE, 'w') as f:
        json.dump(embeddings, f, indent=2)

def get_image_description(image_path):
    url = "http://localhost:8080/v1/chat/completions"
    import base64
    with open(image_path, "rb") as img_file:
        img_bytes = img_file.read()
    img_base64 = "data:image/jpeg;base64," + base64.b64encode(img_bytes).decode()

    payload = {
        "max_tokens": 100,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this image."},
                    {"type": "image_url", "image_url": {"url": img_base64}},
                ],
            }
        ],
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        desc = data["choices"][0]["message"]["content"]
        return desc
    except Exception as e:
        print(f"Error getting description from llama-server: {e}")
        return "No description available"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    filename = file.filename
    save_path = os.path.join(UPLOAD_FOLDER, filename)

    # Save uploaded file
    file.save(save_path)

    # Get description from llama-server
    description = get_image_description(save_path)

    # Save/update embeddings dictionary
    global embeddings
    embeddings[filename] = description
    save_embeddings()

    return jsonify({"filename": filename, "description": description})

@app.route('/search', methods=['POST'])
def search_images():
    data = request.json
    query = data.get('query', '').lower()

    if not query:
        return jsonify({"results": []})

    results = []
    for filename, desc in embeddings.items():
        if query in desc.lower():
            results.append({
                "filename": filename,
                "url": url_for('static', filename=f'uploads/{filename}')
            })

    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True)
