import streamlit as st

storydata_template = {
    "title": "",
    "summary": "",
    "pagecount": 10,
    "character": {
        "provided_image_url": "",
        "character_description": "",
        "character_name": "",
        "character_relation": ""
    },
    "storyelements": {
        "genre": "",
        "setting": "",
        "supportingcharacter": "",
        "plotelements": "",
        "selectedtheme": "",
        "magicalobjects": "",
        "tonemood": ""
    },
    "pages": {
        "page1": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": "",
            "imagefile": "",
            "imageurl": ""
        },
        "page2": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": "",
            "imagefile": "",
            "imageurl": ""
        },
        "page3": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": "",
            "imagefile": "",
            "imageurl": ""
        },
        "page4": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": "",
            "imagefile": "",
            "imageurl": ""
        },
        "page5": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": "",
            "imagefile": "",
            "imageurl": ""
        },
        "page6": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": "",
            "imagefile": "",
            "imageurl": ""
        },
        "page7": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": "",
            "imagefile": "",
            "imageurl": ""
        },
        "page8": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": "",
            "imagefile": "",
            "imageurl": ""
        },
        "page9": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": "",
            "imagefile": "",
            "imageurl": ""
        },
        "page10": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": "",
            "imagefile": "",
            "imageurl": ""
        }
    }
}
    


def initialize_session_states():
    if "storydata" not in st.session_state:
        st.session_state.storydata = storydata_template
    if "title" not in st.session_state:
        st.session_state.title = ""
    if "summary" not in st.session_state:
        st.session_state.summary = ""
    if "character_description" not in st.session_state:
        st.session_state.character_description = ""

    if "awINI" not in st.session_state:
      st.session_state.awINI = 0

    if "awAI" not in st.session_state:
        st.session_state.awAI = 0



