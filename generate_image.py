import streamlit as st
from openai import OpenAI
import json

client = OpenAI(api_key = st.secrets.openai.api_key)
model = "dall-e-3"
size = "1024x1024"
quality = "standard"

def create_image(varPrompt):
  image_response = client.images.generate(
    model=model,
    prompt=varPrompt,
    size=size,
    quality=quality,
    n=1
  )

  generated_image_url = image_response['data'][0]['url']
  return generated_image_url


