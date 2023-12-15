import streamlit as st


def initialize_session_state():
    if 'initialized' not in st.session_state or not st.session_state.initialized:
        # Initialize 'current_step' for navigating between steps
        st.session_state.current_step = 1
        st.session_state.thread_id = None
        st.session_state.message_id = None
        st.session_state.run_id = None

        # Initialize 'storydata' with sub-objects
        st.session_state.storydata = {
            'storyinfo': {'title': '', 'summary': '', 'pagecount': 10},
            'character': {'charactername': '', 'characterrelation': '', 'uploadedimagepath': '', 'characterdescription': '', 'generatedimageurl': ''},
            'storyelements': {'theme': '', 'tone': '', 'setting': '', 'plotelement': '', 'magicalobject': '', 'supportingcharacter': '', 'genre': ''},
            'pages': {f'page{i}': {'narrativeoutline': '', 'narrativetext': '', 'illustrationprompt': '', 'generatedillustrationurl': '', 'seedid': '', 'genid': ''} for i in range(1, 11)}
        }

        # Initialize other form field variables
        form_fields = ['charactername', 'characterrelation', 'uploadedimagepath', 'theme', 'tone', 'setting', 'plotelement', 'magicalobject', 'supportingcharacter', 'genre']
        for field in form_fields:
            st.session_state[field] = ''

        # Mark initialization as done
        st.session_state.initialized = True
