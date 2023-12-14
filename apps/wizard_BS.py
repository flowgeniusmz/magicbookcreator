import streamlit as st
from config import pagesetup as ps

# Helper function for creating narrative and illustration containers
def create_narrative_illustration_container_odd_even(page_num):
    ps.set_blue_header(f"Page {page_num}")
    container = st.container(border = True)  # Create a container for each page
    with container:
        if page_num % 2 == 0:
            cols = st.columns([3, 1, 3])
            with cols[0]:
                exp_narrative = st.expander(f"Page {page_num} Narrative", expanded=True)
                with exp_narrative:
                    st.markdown("Narrative")
            with cols[2]:
                exp_illustration = st.expander(f"Page {page_num} Illustration", expanded=True)
                with exp_illustration:
                    st.markdown("Illustration")
        else:
            cols = st.columns([3, 1, 3])
            with cols[0]:
                exp_illustration = st.expander(f"Page {page_num} Illustration", expanded=True)
                with exp_illustration:
                    st.markdown("Illustration")
            with cols[2]:
                exp_narrative = st.expander(f"Page {page_num} Narrative", expanded=True)
                with exp_narrative:
                    st.markdown("Narrative")


# Define your app_wizard_BS function to display containers
def app_wizard_BS():
    for page_num in range(1, 11):
        create_narrative_illustration_container_odd_even(page_num)
    st.write("Your storybook's narrative and pages in order:")
    st.button("Finalize the Story!", key="btnFinalizeStory")
