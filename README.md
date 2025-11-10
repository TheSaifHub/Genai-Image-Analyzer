Image Analyzer (Gemini + Streamlit)

A lightweight Streamlit app that lets you upload an image, ask a natural-language question about it, and get a response from Google’s Gemini vision model.

✨ Features

Upload .png, .jpg, or .jpeg

Ask any question about the image (objects, text, colors, layout, suggestions, etc.)

Fast responses using gemini-2.0-flash

Simple, single-file app (great for demos & learning)

🧰 Tech Stack

Python 3.10+

Streamlit – UI

google-generativeai – Gemini API client

python-dotenv – loads .env secrets

Pillow (PIL) – image handling

📁 Project Structure
image-analyzer-genai/
├─ app.py                 # your streamlit code (rename if different)
├─ .env                   # holds GEMINI_API_KEY (not committed)
├─ requirements.txt       # pinned dependencies
└─ README.md              # this file

🔐 Prerequisites

Create a Gemini API key

Go to Google AI Studio and generate an API key.

Store it in .env (project root)

# .env
GEMINI_API_KEY=your_api_key_here


Never commit .env to source control. Add it to .gitignore.

📦 Installation
1) Clone & enter the project
git clone <your-repo-url> image-analyzer-genai
cd image-analyzer-genai

2) (Recommended) Create a virtual environment

Windows (PowerShell)

py -m venv .venv
.venv\Scripts\Activate.ps1


macOS / Linux

python3 -m venv .venv
source .venv/bin/activate

3) Install dependencies

Create requirements.txt with:

streamlit>=1.37.0
google-generativeai>=0.8.0
python-dotenv>=1.0.1
Pillow>=10.3.0


Then install:

pip install -r requirements.txt

▶️ Run the App
python -m streamlit run app.py


Open the URL Streamlit prints (usually http://localhost:8501).

🧪 How to Use

Click “Upload an Image” and choose a .png/.jpg/.jpeg.

Type a question in “Enter your Query.”
Examples:

“Summarize what’s in this image.”

“List all visible text.”

“What are possible UI improvements?”

“What’s the mood, and why?”

Click “RESPONSE” to see Gemini’s analysis.