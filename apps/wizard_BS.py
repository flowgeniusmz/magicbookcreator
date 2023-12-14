import streamlit as st

# Helper function for creating narrative and illustration containers
def create_narrative_illustration_container(page_num):
    def even(page_num):
        cols = st.columns([3, 1, 3])
        with cols[0]:
            exp_narrative = st.expander(f"Page {page_num} Narrative", expanded=True)
            with exp_narrative:
                st.markdown("Narrative")
        with cols[2]:
            exp_illustration = st.expander(f"Page {page_num} Illustration", expanded=True)
            with exp_illustration:
                st.markdown("Illustration")

    def odd(page_num):
        cols = st.columns([3, 1, 3])
        with cols[0]:
            exp_illustration = st.expander(f"Page {page_num} Illustration", expanded=True)
            with exp_illustration:
                st.markdown("Illustration")
        with cols[2]:
            exp_narrative = st.expander(f"Page {page_num} Narrative", expanded=True)
            with exp_narrative:
                st.markdown("Narrative")

    if page_num % 2 == 0:
        even(page_num)
    else:
        odd(page_num)


import streamlit as st

# Define your get_wizard_BS function to display containers
def app_wizard_BS():
    for page_num in range(1, 11):
        create_narrative_illustration_container(page_num)
    st.write("Your storybook's narrative and pages in order:")
    st.button("Finalize the Story!", key="btnFinalizeStory")
