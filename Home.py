import streamlit as st
import openai
from openai import OpenAI
from PIL import Image
from apps import wizard_INI as wINI, wizard_BS as wBS
from config import sessionstates as ss, pagesetup as ps

# 0. App Initialization and Setup
st.set_page_config(page_title="MagicBook Creator", page_icon="📚", layout="wide", initial_sidebar_state="collapsed")                                                # Set page config - must be first "st.___" on page
ss.initialize_session_states()                                                                                                                                      # Initialize all session_state variables
ps.set_title("MagicBook", "Creator")                                                                                                                                # Set the title and subtitle using special formating in pagesetup.set_title
ps.set_page_overview("Welcome to MagicBook Creator!", "MagicBook Creator creates a magical storybook based on your inputs in a matter of minutes! It even creates illustrations based on an image you provide! Follow the wizard below to get your storybook today!")

# 1. Wizard Form Initialization
tab_INI, tab_AI, tab_BS, tab_DS = st.tabs(["Initial Story Elements", "AI Story Builder", "Build Summary", "Download Story"])                                         # Initialize the tabs of the wizard form

with tab_INI:
    ps.set_blue_header("Let's get started! First, please fill out the fields below.")   
    wINI.app_wizard_INI()

with tab_AI:
    st.write("A")
    
    
with tab_BS:
    wBS.app_wizard_BS()
    
