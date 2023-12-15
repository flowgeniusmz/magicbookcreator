import streamlit as st

def get_toast_message(type, title):
    
    lowertitle = title.lower()

    if type == "start":
        toast = st.toast(
            f"**{title}: ** Creating {lowertitle}...",
            icon = "⏳"
        )
    
    elif type == "end": 
        toast = st.toast(
            f"**{title}: ** Your {lowertitle} has been created!",
            icon = "✅"
        )

    else:
        toast = st.toast(
            "Invalid syntax", 
            icon = "✅"
        )

    return toast