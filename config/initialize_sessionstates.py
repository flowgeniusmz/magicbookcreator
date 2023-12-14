import streamlit as st


def initialize_session_states():

  if "storydata" not in st.session_state:
    st.session_state.storydata = {}

  if "title" not in st.session_state:
    st.session_state.title = ""

  if "summary" not in st.session_state:
    st.session_state.summary = ""

  if "character_description" not in st.session_state:
    st.session_state.character_description = ""

