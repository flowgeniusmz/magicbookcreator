import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets.openai.api_key)
model = "dall-e-3"
size = "1024x1024"
quality = "standard"

def create_image(varPrompt):
    alert1 = st.toast("Creating character image...", icon="⏳")
    image_response = client.images.generate(
        model=model,
        prompt=varPrompt,
        size=size,
        quality=quality,
        n=1
    )

    generated_image_url = image_response.data[0].url  # Access the URL correctly
    alert2 = st.toast("Character image created!", icon="✅")
    return generated_image_url
