
# 🖼️ AI ImageFinder

**AI-Powered Local Image Search Application**  
Leverage cutting-edge vision-language models to upload, describe, and search your images entirely offline.

---

## 📌 Overview

AI ImageFinder is a Flask-based web application that allows users to:

- Upload image files via drag-and-drop
- Automatically generate captions using **SmolVLM**
- Search images using **natural language queries**
- Match via **semantic similarity** powered by **all-MiniLM-L6-v2**
- Run completely **locally** — no cloud or external APIs required

![Demo Screenshot](imagefinder.jpg)

---

## 🧠 Architecture

| Component        | Description                                                      |
|------------------|------------------------------------------------------------------|
| **Flask Backend** | Handles image uploads, search, and serving static content        |
| **SmolVLM**       | Generates image descriptions via `llama-server`                  |
| **MiniLM Model**  | Encodes descriptions and queries for semantic matching locally   |
| **Frontend (HTML/JS/CSS)** | Modern UI with upload area, search input, theme toggle |

---

## 🚀 Installation

### ✅ Prerequisites

- Python ≥ 3.8
- Git & Git LFS
- Virtualenv (optional but recommended)

### 📦 Step-by-Step Setup

```bash
# Clone the repository
git clone https://github.com/MohdWaheed21/image-search-app
cd image-search-app

# Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 🧠 Download Models

### Install llama-cpp

Winget (Windows)
```bash
winget install llama.cpp
```
Homebrew (Mac and Linux)
```bash
brew install llama.cpp
```

#### SmolVLM for image captions:

```bash
llama-server -hf ggml-org/SmolVLM-500M-Instruct-GGUF
```
_Keep this running on `localhost:8080`._

#### Sentence Transformer for search:
```bash
git lfs install
mkdir -p models
git clone https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 models/all-MiniLM-L6-v2
```

---

## 🖥️ Running the App

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## 🛠️ Usage Guide

### ➕ Upload Images

- Supported: JPG, PNG, WEBP
- Drag and drop or select from disk
- Each image gets described via SmolVLM

### 🔍 Search by Description

- Use phrases like `"a dog playing in snow"`
- Images are returned by semantic similarity
- Match confidence displayed

### 🌗 Theme Toggle

- Click the 🌓 icon to switch dark/light modes

---

## 🧪 Troubleshooting

| Issue | Solution |
|-------|----------|
| ❌ No captions generated | Ensure `llama-server` is running on port 8080 |
| ❌ "Model not found" | Ensure `models/all-MiniLM-L6-v2` exists and contains model files |
| 🐢 Slow search/upload | Reduce image size or raise similarity threshold in `app.py` |

---

## 🗂 Project Structure

```text
├── app.py                 # Main Flask app
├── requirements.txt
├── static/
│   ├── style.css
│   └── uploads/           # Uploaded images
├── templates/
│   └── index.html
├── models/
│   └── all-MiniLM-L6-v2/  # Cloned SentenceTransformer
├── embeddings.json        # Stores image captions
└── README.md
```

---

## 📄 License

This project is licensed under the **MIT License**.  
Free for personal and commercial use.

---

## 📬 Contact & Support

- Twitter: [@Mohd Waheed](https://www.linkedin.com/in/mohd-waheed-168452317/)
- Twitter: [@Vighneshwar kuru](https://www.linkedin.com/in/vighneshwarkuru/)

---

> **Note**: Running this app on large image datasets may require 8GB+ RAM for smooth operation.
