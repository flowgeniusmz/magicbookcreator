import streamlit as st
from apps import wizard_INI as wINI, wizard_BS as wBS, wizard_AI as wAI
from config import sessionstates as ss, pagesetup as ps

# 0. App Initialization and Setup
st.set_page_config(page_title="MagicBook Creator", page_icon="📚", layout="wide", initial_sidebar_state="collapsed")
ss.initialize_session_states()  # Initialize all session_state variables
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

# Additional code for other tabs and functionality
