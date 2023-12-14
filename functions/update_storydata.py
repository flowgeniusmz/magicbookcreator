import streamlit as st


def update_story_data(key, value):
    """
    Update the story_data JSON with the provided key and value.

    Args:
        key (str): The key where the value should be updated.
        value: The value to update.
    """
    if key in st.session_state.storydata:
        st.session_state.storydata[key] = value
    else:
        print(f"Key '{key}' not found in story_data JSON.")


def get_story_data():
    data = st.session_state.storydata
    return data


