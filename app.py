import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image

# Load .env variables
load_dotenv()

# Page settings
st.set_page_config(
    page_title="Gemini Image Analyzer",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS Styling
st.markdown("""
    <style>
        .title {
            font-size: 40px;
            font-weight: 700;
            text-align: center;
            margin-bottom: 5px;
        }
        .subtitle {
            font-size: 18px;
            text-align: center;
            color: #555;
            margin-bottom: 25px;
        }
        .stTextInput>div>div>input {
            border: 2px solid #4CAF50 !important;
            border-radius: 8px;
        }
        .css-1kyxreq, .stButton>button {
            background-color: #4CAF50 !important;
            color: white !important;
            border-radius: 8px !important;
            font-size: 18px !important;
            padding: 10px 20px !important;
        }
        .stButton>button:hover {
            background-color: #45a049 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Titles
st.markdown('<div class="title">🧠 Gemini Image Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Analyze images using Google Gemini Vision</div>', unsafe_allow_html=True)

# Load Gemini API Key
gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

# File Upload
uploaded_file = st.file_uploader("📤 Upload an Image", type=['png', 'jpg', 'jpeg'])

# Show Image
if uploaded_file:
    st.image(Image.open(uploaded_file), use_column_width=True)

# Prompt
prompt = st.text_input("💬 Enter your query about the image:")

# Response Button
if st.button("🔍 Analyze Image"):
    if not uploaded_file:
        st.warning("⚠️ Please upload an image.")
    elif not prompt.strip():
        st.warning("⚠️ Please enter a question.")
    else:
        try:
            img = Image.open(uploaded_file)
            model = genai.GenerativeModel("gemini-2.0-flash")  # Requires Google Cloud key

            with st.spinner("Analyzing image... ⏳"):
                response = model.generate_content([prompt, img])

            st.subheader("📌 Response:")
            st.write(response.text or "_No text returned._")

        except Exception as e:
            st.error(f"❌ Something went wrong: {e}")
