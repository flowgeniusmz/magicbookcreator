import streamlit as st
from openai import OpenAI
from functions import create_storydetails as genstory

def app_wizard_AI():
  wizardstoryoutline = genstory.create_story_details()
  st.write(wizardstoryoutline)
