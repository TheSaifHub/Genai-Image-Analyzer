# all packages are installed

import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

st.title("Generative Ai Image Analyzer")

gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key = gemini_api_key)

uploaded_file = st.file_uploader("Upload an Image", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    st.image(Image.open(uploaded_file))
    
prompt = st.text_input("Enter your query:")

if st.button("RESPONSE"):
    if uploaded_file is None:
        st.warning("Please upload an image first!")
    elif not prompt.strip():
        st.warning("Please enter a query first!")
    else:
        try:
            img = Image.open(uploaded_file)
            model = genai.GenerativeModel("gemini-2.0-flash")
            response = model.generate_content([prompt, img])
            st.markdown(response.text or "_No text returned._")
        except Exception as e:
            st.error(f"Something went wrong: {e}")