import streamlit as st
import openai
from openai import OpenAI
from PIL import Image
from functions import create_characterdescription as chardesc, create_tempfile as tfile, generate_image as genimg, update_storydata as sd
from config import pagesetup as ps, sessionstates as ss

# 0. App Initialization and Setup
st.set_page_config(page_title="MagicBook Creator", page_icon="📚", layout="wide", initial_sidebar_state="collapsed")                                                # Set page config - must be first "st.___" on page
ss.initialize_session_States()                                                                                                                                      # Initialize all session_state variables
ps.set_title("MagicBook", "Creator")                                                                                                                                # Set the title and subtitle using special formating in pagesetup.set_title
ps.set_page_overview("Welcome to MagicBook Creator!", "MagicBook Creator creates a magical storybook based on your inputs in a matter of minutes! It even creates illustrations based on an image you provide! Follow the wizard below to get your storybook today!")

# 1. Wizard Form Initialization
tab_INI, tab_AI, tab_BS, tab_DS = st.tabs(["Initial Story Elements", "AI Story Builder", "Build Summary", "Download Story"])                                         # Initialize the tabs of the wizard form

# 2. Wizard Form - Initial Story Elements (INI)
with tab_INI:
  st.write("a")
  
# 3. Wizard Form - AI Story Builder (AI)
with tab_AI:
  st.write("a")

# 4. Wizard Form - Build Summary (BS)
with tab_BS:
  st.write("a")

# 5. Wizard Form - Download Story (DS)
with tab_DS:
  st.write("a")
