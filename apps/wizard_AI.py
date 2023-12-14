import streamlit as st
from openai import OpenAI
from functions import create_storydetails as genstory, update_storydata as sdata


storybook_data = st.session_state.storydata

def app_wizard_AI():
  
  st.write(storybook_data)
  wizardstoryoutline = genstory.create_story_details(storybook_data)
  st.write(wizardstoryoutline)
  
