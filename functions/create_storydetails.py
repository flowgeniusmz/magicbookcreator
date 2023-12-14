import streamlit as st
from openai import OpenAI
from functions import update_storydata as sdata
from utils import openai_assistant as oaiAsst


def create_story_details():
  client = OpenAI(api_key = st.secrets.openai.api_key)
  assistantid = "asst_f9LcmBeJRI1VeVk4d1gQ0V79"
  threadid = client.beta.threads.create().id
  storybookdata = sdata.get_story_data_nopages()
  instructions = f"""
  Create a 10-page storybook outline, narrative, and illustration prompts using the following details:
  
  {storybookdata}
  
  REMINDER: Only return the final json output.
  """
  messageid = oaiAsst.create_thread_message("user", instructions, threadid)
  response = oaiAsst.run_assistant(assistantid, threadid)
  return response


