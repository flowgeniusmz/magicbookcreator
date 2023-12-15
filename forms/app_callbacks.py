import streamlit as st
from forms.util_createtempfile import create_temp_file_for_uploaded_image


def on_form_submit():
    if 'uploadedimage' in st.session_state:
        tmp_file_path = create_temp_file_for_uploaded_image(st.session_state.uploadedimage)
        if tmp_file_path:
            # Update the session state with the path of the uploaded image
            st.session_state.storydata['character']['uploadedimagepath'] = tmp_file_path

    # Example of capturing form data (adjust according to actual form fields)
    st.session_state.storydata['character']['charactername'] = st.session_state.charactername
    st.session_state.storydata['character']['characterrelation'] = st.session_state.characterrelation
    st.session_state.storydata['storyelements']['theme'] = st.session_state.theme
    st.session_state.storydata['storyelements']['tone'] = st.session_state.tone
    st.session_state.storydata['storyelements']['setting'] = st.session_state.setting
    st.session_state.storydata['storyelements']['plotelement'] = st.session_state.plotelement
    st.session_state.storydata['storyelements']['magicalobject'] = st.session_state.magicalobject
    st.session_state.storydata['storyelements']['supportingcharacter'] = st.session_state.supportingcharacter
    st.session_state.storydata['storyelements']['genre'] = st.session_state.genre

    # Navigate to the next step
    st.session_state.current_step = 2
    st.rerun()

