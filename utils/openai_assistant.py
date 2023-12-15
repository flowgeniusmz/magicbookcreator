import streamlit as st
from openai import OpenAI
import time

client = OpenAI(api_key = st.secrets.openai.api_key)

def create_thread_message(varRole, varContent, varThreadId):
  thread_message = client.beta.threads.messages.create(
    role=varRole,
    content=varContent,
    thread_id=varThreadId
  )
  thread_message_id = thread_message.id
  st.session_state.threadid = varThreadId
  return thread_message_id

def run_assistant(varAssistantId, varThreadId):
  run = client.beta.threads.runs.create(
    thread_id=varThreadId,
    assistant_id=varAssistantId
  )
  st.session_state.runid = run.id
  while run.status == "in-progress" or run.status == "queued":
    time.sleep(0.5)
    run = client.beta.threads.runs.retrieve(
      thread_id=varThreadId,
      run_id=run.id
      )

    if run.status == "completed": 
      messages = client.beta.threads.messages.list(
        thread_id = varThreadId,
        order = "asc"
      )
      for message in messages:
        if message.role == "assistant":
          msgcontent = message.content[0].text.value if message.content else None
          return msgcontent
        
    
