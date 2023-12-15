import streamlit as st
import openai
from openai import OpenAI

client = OpenAI(api_key = st.secrets.openai.api_key)


def app_wizard_AI():
    st.write("AI Story Builder")

    # Check if story details are available in session state
    if 'storydatadetails' in st.session_state and st.session_state.storydatadetails is not None:
        story_details = st.session_state.storydatadetails

        # Display the story details
        st.write("Here are your story details:")
        st.json(story_details)  # Display the story details in JSON format, or format as needed

        # Additional code to allow further editing or processing of story details
        # ...

    else:
        st.warning("Please complete the Initial Story Elements to generate the story details.")
        # Optionally, provide a button or link to go back to the Initial Story Elements tab
        # ...

    threadmessagelist = client.beta.threads.messages.list(
        thread_id = st.session_state.threadid,
        order = "asc"
    )
    st.markdown(threadmessagelist)

