import streamlit as st
from forms.app_callbacks import on_form_submit


def get_form_storyelements():
    with st.form("formStoryElements"):

        # File Uploader for image upload
        uploaded_img = st.file_uploader(
            label =  "Upload an image of the main character", 
            type = ['png', 'jpg', 'jpeg', 'gif'],
            key = "uploadedimage"
        )

        # Divider - separate image upload and fields
        st.divider()

        # Form fields (text or select) put into 3 columns
        cols_storyelements = st.columns(3)
        with cols_storyelements[0]:
            se_charactername = st.text_input(
                label = "Character Name",
                key = "charactername",
                help = "Enter the name of the main character for whom the story is for or about.",
            )

            se_characterrelationship = st.text_input(
                label = "Character Relation",
                key = "characterrelation",
                help = "Enter your relation with the main character for whom the story is about."
            )
            se_theme = st.selectbox(
                label = "Theme",
                key = "theme",
                help = "Select a theme or choose 'surprise me'",
                options = ["Friendship", "Courage", "Kindness", "Discovery", "Teamwork", "Surprise Me"]
            )
        with cols_storyelements[1]:
            se_setting = st.selectbox(
                label = "Setting",
                key = "setting",
                help = "Select a setting or choose 'surprise me'",
                options = ["Enchanted Forest", "Outer Space", "Kingdom", "Under the Sea", "Mystical Mountain", "Surprise Me"]
            )

            se_genre = st.selectbox(
                label = "Genre",
                key = "genre",
                help = "Select a genre or choose 'surprise me'",
                options = ["Adventure", "Fairy Tale", "Animal Story", "Space Exploration", "Magical Fantasy", "Surprise Me"]
            )

            se_tone = st.selectbox(
                label = "Tone / Mood",
                key = "tone",
                help = "Select a tone or choose 'surprise me'",
                options = ["Joyful", "Exciting", "Mysterious", "Playful", "Heartwarming", "Surprise Me"]
            )

        with cols_storyelements[2]:
            se_supportingcharacter = st.selectbox(
                label = "Supporting Character",
                key = "supportingcharacter",
                help = "Select a supporting character or choose 'surprise me'",
                options = ["Wise Owl", "Funny Clown", "Talking Robot", "Friendly Dragon", "Mischievous Monkey", "Surprise Me"]
            )

            se_plotelement = st.selectbox(
                label = "Plot Elements",
                key = "plotelement",
                help = "Select a plot element or choose 'surprise me'",
                options = ["A Hidden Treasure", "A Grand Festival", "A Magic Spell", "A Daring Rescue", "A Secret Door", "Surprise Me"]
            )

            se_magicalobject = st.selectbox(
                label = "Magical Object",
                key = "magicalobject",
                help = "Select a magical object or choose 'surprise me'",
                options = ["Magic Wand", "Enchanted Mirror", "Golden Key", "Flying Carpet", "Invisible Cloak", "Surprise Me"]
            )

        submitted = st.form_submit_button(
            label = "Submit Story Elements", 
            on_click = on_form_submit
        )