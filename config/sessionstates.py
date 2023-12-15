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
    # Initialize 'storydata' if not present in session state
    if "storydata" not in st.session_state:
        st.session_state.storydata = storydata_template

    if "storydatadetails" not in st.session_state:
        st.session_state.storydatadetails = {}

    if "threadid" not in st.session_state:
        st.session_state.threadid = ""

    if "runid" not in st.session_state:
        st.session_state.runid = ""
    
    if "uploadedimage" not in st.session_state:
        st.session_state.uploadedimage = ""


    # Initialize top-level elements
    for key in ['title', 'summary', 'pagecount']:
        if key not in st.session_state:
            st.session_state[key] = storydata_template[key]

    # Initialize 'character' elements
    character_keys = ['provided_image_url', 'character_description', 'character_name', 'character_relation']
    for key in character_keys:
        if f"character_{key}" not in st.session_state:
            st.session_state[f"character_{key}"] = storydata_template['character'][key]

    # Initialize 'storyelements' elements
    storyelements_keys = ['genre', 'setting', 'supportingcharacter', 'plotelements', 'selectedtheme', 'magicalobjects', 'tonemood']
    for key in storyelements_keys:
        if f"storyelements_{key}" not in st.session_state:
            st.session_state[f"storyelements_{key}"] = storydata_template['storyelements'][key]

    # Initialize 'pages' elements
    for i in range(1, storydata_template['pagecount'] + 1):
        page_keys = ['narrative', 'imageprompt', 'seedid', 'genid', 'imagefile', 'imageurl']
        for key in page_keys:
            if f"page{i}_{key}" not in st.session_state:
                st.session_state[f"page{i}_{key}"] = storydata_template['pages'][f'page{i}'][key]


def initialize_session_states_old():
    if "storydata" not in st.session_state:
        st.session_state.storydata = storydata_template
    if "title" not in st.session_state:
        st.session_state.title = ""
    if "summary" not in st.session_state:
        st.session_state.summary = ""
    if "character_description" not in st.session_state:
        st.session_state.character_description = ""



