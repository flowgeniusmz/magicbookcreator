import streamlit as st
from apps import wizard_INI as wINI, wizard_BS as wBS, wizard_AI as wAI
from config import sessionstates as ss, pagesetup as ps
from PIL import Image


# 0. App Initialization and Setup
st.set_page_config(page_title="MagicBook Creator", page_icon="📚", layout="wide", initial_sidebar_state="collapsed")

if "initialized" not in st.session_state:
    st.session_state.initialized = True
    ss.initialize_session_states()
    
ps.set_title("MagicBook", "Creator")
ps.set_page_overview("Welcome to MagicBook Creator!", "MagicBook Creator creates a magical storybook...")

# 1. Wizard Form Initialization
tab_INI, tab_AI, tab_BS, tab_DS = st.tabs(["Initial Story Elements", "AI Story Builder", "Build Summary", "Download Story"])

with tab_INI:
    ps.set_blue_header("Let's get started! First, please fill out the fields below.")
    wINI.app_wizard_INI()

with tab_AI:
    wAI.app_wizard_AI()

with tab_BS:
    wBS.app_wizard_BS()
    st.write(st.session_state.threadid)

# Additional code for other tabs and functionality

cont = st.container(border=True)
with cont:
    if "uploadedimage" not in st.session_state or st.session_state.uploadedimage == "":
        warning_noimage = st.warning("Please upload an image to continue")
    else:
        expd = st.expander("Character Images", expanded=True)
        with expd:
            col = st.columns ([3,1,3])
            with col[0]:
                openimage = Image.open(st.session_state.uploadedimage)
                st.image(openimage, "Uploaded Image")
            with col[2]:
                openimage2 = Image.open(st.session_state.storydata["character"]["character_image"])
                st.image(openimage2, "Created Image")
            st.markdown(f"""**Character Description:** {st.session_state.storydata["character"]["character_description"]}""")
            
            
