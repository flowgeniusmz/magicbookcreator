import streamlit as st

def format_story_data():
    # Assuming your story data is stored in st.session_state.storydata
    story_data = st.session_state.storydata

    # Format the data as needed for the create_story_details function
    formatted_data = {
        "title": story_data["title"],
        "summary": story_data["summary"],
        "character": story_data["character"],
        "storyelements": story_data["storyelements"]
    }
    return formatted_data
