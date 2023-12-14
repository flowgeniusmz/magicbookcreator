import streamlit as st
from openai import OpenAI
from functions import create_storydetails as genstory, update_storydata as sdata

if "awAI" not in st.session_state:
  st.session_state.awAI = 0

wINIcomplete = st.session_state.awINI

storybook_data = st.session_state.storydata

def app_wizard_AI():
  if wINIcomplete=1
    st.write(storybook_data)
    wizardstoryoutline = genstory.create_story_details(storybook_data)
    st.write(wizardstoryoutline)
  else:
    st.write("Complete INI page")
 
