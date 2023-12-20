import streamlit as st
import base64
import requests
from functions import update_storydata as sdata

### OVERVIEW: Get_Character_Description function makes a https request.post call to OpenAI chat completions using OpenAI Vision model. An image is provided and OpenAI Vision can look at the image and provide a characer description. ###

# 1. Setup and Variables
openai_api_key = st.secrets.openai.api_key              # Used to formulate authorization header
model = "gpt-4-vision-preview"                            # Used in request payload
url = "https://api.openai.com/v1/chat/completions"        # Used in request.post
contenttype = "application/json"                          # Used in request headers
authorization = f"Bearer {openai_api_key}"                # Used in request headers

# 2. Set Instructions (System Message)
sys_instructions_imageanddetails = """As an expert in image analysis and descriptive content generation using OpenAI's GPT-4 Vision API, your task is to create a personalized narrative framework for a children's storybook based on a detailed JSON payload provided by the user. This payload includes an image of the main character, along with specific story elements like character names, themes, and settings. Your responsibilities are as follows:\n\nAnalyze the uploaded image, focusing on the main character depicted.\nUse the details from the JSON payload (character name, relation, theme, genre, setting, etc.) to enrich the narrative context.\nGenerate a captivating title for the storybook that aligns with the given theme and setting.\nCraft a brief summary of the story, integrating the plot elements and secondary characters as suggested in the payload.\nCreate a detailed, imaginative description of the main character, considering the character's name, relation, and other attributes provided.\nIteratively refine each element (title, summary, character description) to enhance their quality, detail, and fit within the whimsical and magical tone of a children's storybook.\nRETURN / OUTPUT: Deliver the final output in this format:\n\"{\n'Title': '{{Story Title}}',\n'Summary': '{{Story Summary}}',\n'Character_Description': '{{Character Description}}'\n}\",\nwhere each placeholder is replaced with your crafted content.\nConsistently adhere to these guidelines:\n\nPerform all steps internally, leveraging your image analysis and creative content generation capabilities.\nInteract with the user only for delivering the final output.\nEnsure all content (title, summary, character description) is suitable for a children's storybook, imbued with creativity, charm, and whimsy.\nBase all elements on the provided image and details in the JSON payload, to create a cohesive and engaging story.\nAim for a style reminiscent of Disney or Pixar narratives, characterized by vivid, imaginative, and engaging storytelling.\nProvide only the text content (title, summary, character description) as the final output."""

user_instruction = "Provide the title and summary based on the story data provided. Then using the image_url provided describe the main person in this image. Provide the json output. /n```json"

# 3. Encode Image Function (Used within Get_Character_Description)
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# 4. Get Character Description Function
def get_character_description(image_path, story_elements): 
  alert1 = st.toast("Creating character description...", icon="⏳")
  base64_image = encode_image(image_path)
  img_url = f"data:image/jpeg;base64,{base64_image}"
  
  msg_system = {
    "role": "system",
    "content": sys_instructions_imageanddetails
  }

  msg_user = {
    "role": "user",
    "content": [
      {"type": "text", "text": f"{user_instruction}: {story_elements}"},
      {"type": "image_url", "image_url": {"url": img_url}}
    ]
  }

  msgs = [msg_system, msg_user]
  headers = {"Content-Type": contenttype, "Authorization": authorization}
  payload = {"model": model, "messages": msgs, "max_tokens": 2500, "temperature": 0}
  response = requests.post(url=url, headers=headers, json=payload)
  response_data = response.json()
  characterdescription = response_data['choices'][0]['message']['content']
  sdata.update_story_data("character.character_description", characterdescription)                                  # Update the story data json object with characterdescription
  alert2 = st.toast("Character description created!", icon="✅")

  return characterdescription
    
