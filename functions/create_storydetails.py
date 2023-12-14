import streamlit as st
from openai import OpenAI
from functions import update_storydata as sdata
from utils import openai_assistant as oaiAsst

client = OpenAI(api_key = st.secrets.openai.api_key)
assistantid = st.secrets.openai.assistant_key_magicbook
threadid = client.beta.threads.create().id


def create_story_details(varStoryData):
  alert1 = st.toast("Creating story details...", icon="⏳")
  instructions = f"""
  Create a 10-page storybook outline, narrative, and illustration prompts using the following details:
  
  {varStoryData}
  
  REMINDER: Only return the final json output.
  """
  messageid = oaiAsst.create_thread_message("user", instructions, threadid)
  response = oaiAsst.run_assistant(assistantid, threadid)
  alert2 = st.toast("Story details created!", icon="✅")
  return response


 
