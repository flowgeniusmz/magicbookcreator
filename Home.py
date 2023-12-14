import streamlit as st
import openai
from openai import OpenAI
from PIL import Image
from character_description import get_character_description
from temp_file import get_tempfile_path
from generate_image import create_image
from story_data import update_story_data
from apps import wizard_INI as wINI
from config import sessionstates as ss

# 0. Set page config
st.set_page_config(page_title = "MagicBook Creator", page_icon = "📚", layout = "wide", initial_sidebar_state = "collapsed")
ss.initialize_session_states()

st.title('Storybook Creator')
st.markdown("Welcome to the story book creator, a place where AI technology can make any person on the planet the main character! Don't believe me? Give it a shot for yourself!")
"---"
tab_INI, tab_AI, tab_BS, tab_DS = st.tabs(["Initial Story Elements", "AI Story Builder", "Build Summary", "Download Story"])

with tab_INI:
    wINI.app_wizard_INI()

with tab_AI:
    st.write("A")
    
    
with tab_BS:
    
    container0 = st.container(border=True)
    with container0: 
        st.title('Title Placeholder')
        st.markdown('Summary Placeholder')
        
    container1 = st.container(border=True)
    with container1: 
        cc1 = st.columns([3,1,3])
        with cc1[0]:
            exp11 = st.expander("Page 1 Narrative", expanded = True)
            with exp11: 
                st.markdown("Narrative")
        with cc1[2]: 
            exp12 = st.expander("Page 1 Illustration", expanded = True)
            with exp12:
                st.markdown("Illustration")
        
    container2 = st.container(border=True)
    with container2: 
        cc2 = st.columns([3,1,3])
        with cc2[0]:
            exp21 = st.expander("Page 2 Illustration", expanded = True)
            with exp21:
                st.markdown("Illustration")
                
        with cc2[2]: 
            exp22 = st.expander("Page 2 Narrative", expanded = True)
            with exp22: 
                st.markdown("Narrative")
        
    container3 = st.container(border=True)
    with container3: 
        cc3 = st.columns([3,1,3])
        with cc3[0]:
            exp31 = st.expander("Page 3 Narrative", expanded = True)
            with exp31: 
                st.markdown("Narrative")
        with cc3[2]: 
            exp32 = st.expander("Page 3 Illustration", expanded = True)
            with exp32:
                st.markdown("Illustration")
            
    container4 = st.container(border=True)
    with container4: 
        cc4 = st.columns([3,1,3])
        with cc4[0]:
            exp41 = st.expander("Page 4 Illustration", expanded = True)
            with exp41:
                st.markdown("Illustration")
                
        with cc4[2]: 
            exp42 = st.expander("Page 4 Narrative", expanded = True)
            with exp42: 
                st.markdown("Narrative")
            
    container5 = st.container(border=True)
    with container5: 
        cc5 = st.columns([3,1,3])
        with cc5[0]:
            exp51 = st.expander("Page 5 Narrative", expanded = True)
            with exp51: 
                st.markdown("Narrative")
                
        with cc5[2]: 
            exp52 = st.expander("Page 5 Illustration", expanded = True)
            with exp52:
                st.markdown("Illustration")
            
    container6 = st.container(border=True)
    with container6: 
        cc6 = st.columns([3,1,3])
        with cc6[0]:
            exp61 = st.expander("Page 6 Illustration", expanded = True)
            with exp61:
                st.markdown("Illustration")
                
        with cc6[2]: 
            exp62 = st.expander("Page 6 Narrative", expanded = True)
            with exp62: 
                st.markdown("Narrative")
            
    container7 = st.container(border=True)
    with container7: 
        cc7 = st.columns([3,1,3])
        with cc7[0]:
            exp71 = st.expander("Page 7 Narrative", expanded = True)
            with exp71: 
                st.markdown("Narrative")
                
        with cc7[2]: 
            exp72 = st.expander("Page 7 Illustration", expanded = True)
            with exp72:
                st.markdown("Illustration")
            
    container8 = st.container(border=True)
    with container8: 
        cc8 = st.columns([3,1,3])
        with cc8[0]:
            exp81 = st.expander("Page 8 Illustration", expanded = True)
            with exp81:
                st.markdown("Illustration")
                
        with cc8[2]: 
            exp82 = st.expander("Page 8 Narrative", expanded = True)
            with exp82: 
                st.markdown("Narrative")
            
    container9 = st.container(border=True)
    with container9: 
        cc9 = st.columns([3,1,3])
        with cc9[0]:
            exp91 = st.expander("Page 9 Narrative", expanded = True)
            with exp91: 
                st.markdown("Narrative")
                
        with cc9[2]: 
            exp92 = st.expander("Page 9 Illustration", expanded = True)
            with exp92:
                st.markdown("Illustration")
            
    container10 = st.container(border=True)
    with container10: 
        cc10 = st.columns([3,1,3])
        with cc10[0]:
            exp101 = st.expander("Page 10 Illustration", expanded = True)
            with exp101:
                st.markdown("Illustration")
                
        with cc10[2]: 
            exp102 = st.expander("Page 10 Narrative", expanded = True)
            with exp102: 
                st.markdown("Narrative")
    

    st.write("Your storybook's narrative and pages in order:")

    st.button("Finalize the story")
