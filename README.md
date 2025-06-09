
# Image Search App

This web app allows you to upload images, generates descriptive summaries for them using the SmolVLM model via a local llama-server, and lets you search images based on these summaries.

## Features

- Upload images and generate descriptive embeddings (summaries).
- Store image metadata in a JSON file.
- Search images by text query matching the generated summaries.
- View matched images without displaying their descriptions on search results.

## Tech Stack

- Python (Flask)
- HTML, CSS, JavaScript
- SmolVLM model served by llama-server (`ggml-org/SmolVLM-500M-Instruct-GGUF`)

## Setup Instructions

### Prerequisites

- Python 3.x installed
- `pip` package manager
- `llama-server` running with SmolVLM model:
  ```bash
  llama-server -hf ggml-org/SmolVLM-500M-Instruct-GGUF
  ```
- Required Python packages:
  ```bash
  pip install flask requests
  ```

### Running the App

1. Clone or download this repo.
2. Start the llama-server with the SmolVLM model.
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Open your browser and visit:
   ```
   http://127.0.0.1:5000
   ```

## Usage

- **Upload:** Select one or more images to upload. The app generates descriptions and stores them.
- **Search:** Enter a text query to find related images based on the stored descriptions.
- Matching images will appear without the descriptive text shown.

## Folder Structure

```
image-search-app/
├── app.py
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── embeddings.json
├── README.md
```

## Troubleshooting

- Ensure llama-server is running before uploading images.
- Check network access if descriptions are not generated.
- Use supported image formats (e.g., PNG, JPG).

---

Feel free to contribute or report issues!
