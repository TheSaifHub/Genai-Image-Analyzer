# # all packages are installed

# import os
# import streamlit as st
# import google.generativeai as genai
# from dotenv import load_dotenv
# from PIL import Image

# load_dotenv()

# st.title("Generative Ai Image Analyzer")

# gemini_api_key = os.getenv("GEMINI_API_KEY")
# genai.configure(api_key = gemini_api_key)

# uploaded_file = st.file_uploader("Upload an Image", type=['png', 'jpg', 'jpeg'])

# if uploaded_file is not None:
#     st.image(Image.open(uploaded_file))
    
# prompt = st.text_input("Enter your query:")

# if st.button("RESPONSE"):
#     if uploaded_file is None:
#         st.warning("Please upload an image first!")
#     elif not prompt.strip():
#         st.warning("Please enter a query first!")
#     else:
#         try:
#             img = Image.open(uploaded_file)
#             model = genai.GenerativeModel("gemini-2.0-flash")
#             response = model.generate_content([prompt, img])
#             st.markdown(response.text or "_No text returned._")
#         except Exception as e:
#             st.error(f"Something went wrong: {e}")



import os
import base64
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("OpenAI Image Analyzer (GPT-4o-mini Vision)")

uploaded_file = st.file_uploader("Upload an Image", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

prompt = st.text_input("Enter your query about the image:")

if st.button("GET RESPONSE"):
    if uploaded_file is None:
        st.warning("Please upload an image first.")
    elif not prompt.strip():
        st.warning("Please type your question.")
    else:
        try:
            # Convert image to base64
            image_bytes = uploaded_file.getvalue()
            image_b64 = base64.b64encode(image_bytes).decode("utf-8")

            # Base64 → data URL
            image_base64_url = f"data:image/jpeg;base64,{image_b64}"

            # API call
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": image_base64_url
                                }
                            }
                        ],
                    }
                ],
                max_tokens=300
            )

            # FIX → content is an attribute, not a dict
            answer = response.choices[0].message.content

            st.subheader("Response:")
            st.write(answer)

        except Exception as e:
            st.error(f"Error: {e}")
