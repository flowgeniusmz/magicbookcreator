import streamlit as st
from app_steps import handle_step1, handle_step2, handle_step3
from app_sessionstates import initialize_session_state

def main():
    initialize_session_state()
    st.title("Storybook Creator")

    if st.session_state.current_step == 1:
        handle_step1()
    elif st.session_state.current_step == 2:
        handle_step2()
    elif st.session_state.current_step == 3:
        handle_step3()

if __name__ == "__main__":
    main()
