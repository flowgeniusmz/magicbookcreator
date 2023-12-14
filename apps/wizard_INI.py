import streamlit as st
from PIL import Image
from functions import create_tempfile as tf, create_characterdescription as chardesc, generate_image as genimg, create_storydetails as sdetails

def app_wizard_INI():
    with st.form("Initial Story Elements"):
        # File uploader for character image
        uploaded_img = st.file_uploader("Upload a picture of the person/pet you'd like on a card, board, or coloring page", type=['png', 'jpg', 'jpeg', 'gif'])

        if uploaded_img is not None:
            image = Image.open(uploaded_img)
            image_path = tf.get_tempfile_path(image)
            character_description = chardesc.get_character_description(image_path)
            character_image = genimg.create_image(character_description)

            exp_images = st.expander("View Uploaded and Character Images", expanded=False)
            with exp_images:
                cc = st.columns([3,1,3])
                with cc[0]:
                    st.image(image, "Uploaded Image")
                with cc[2]:
                    st.image(character_image, "Created Image")
                st.markdown("**Character Description**")
                st.markdown(character_description)

            # Update character description and image URL in session state
            st.session_state.storydata["character"]["character_description"] = character_description
            st.session_state.storydata["character"]["provided_image_url"] = character_image

        else:
            st.warning("Please upload at least one image of your loved one.")

        # Form fields for story elements
        cols_storyelements = st.columns(3)
        with cols_storyelements[0]:
            character_name = st.text_input("Character Name", key="storydata['character']['character_name']")
            genre = st.selectbox("Choose the Genre", options=["Adventure", "Fairy Tale", "Animal Story", "Space Exploration", "Magical Fantasy", "Surprise Me"], key="storydata['storyelements']['genre']")
            supporting_character = st.selectbox("Choose A Supporting Character", options=["Wise Owl", "Funny Clown", "Talking Robot", "Friendly Dragon", "Mischievous Monkey", "Surprise Me"], key="storydata['storyelements']['supportingcharacter']")

        with cols_storyelements[1]:
            character_relationship = st.text_input("Relation to Character (e.g. daughter, mother, etc.)", key="storydata['character']['character_relation']")
            tone = st.selectbox("Choose the Theme", options=["Joyful", "Exciting", "Mysterious", "Playful", "Heartwarming", "Surprise Me"], key="storydata['storyelements']['tonemood']")
            plot_elements = st.selectbox("Choose Plot Elements", options=["A Hidden Treasure", "A Grand Festival", "A Magic Spell", "A Daring Rescue", "A Secret Door", "Surprise Me"], key="storydata['storyelements']['plotelements']")

        with cols_storyelements[2]:
            theme = st.selectbox("Choose the Theme", options=["Friendship", "Courage", "Kindness", "Discovery", "Teamwork", "Surprise Me"], key="storydata['storyelements']['selectedtheme']")
            setting = st.selectbox("Choose the Setting", options=["Enchanted Forest", "Outer Space", "Kingdom", "Under the Sea", "Mystical Mountain", "Surprise Me"], key="storydata['storyelements']['setting']")
            magical_objects = st.selectbox("Choose Magical Objects", options=["Magic Wand", "Enchanted Mirror", "Golden Key", "Flying Carpet", "Invisible Cloak", "Surprise Me"], key="storydata['storyelements']['magicalobjects']")

        submit_storyelements = st.form_submit_button("Submit Story Elements and Create MagicBook!")

        if submit_storyelements:
            st.write("Data Submitted")
            
            if 'character_description' in st.session_state.storydata["character"] and 'provided_image_url' in st.session_state.storydata["character"]:
                # Format the story data
                formatted_story_data = sdataformat.format_story_data()
                # Create story details
                story_details = sdetails.create_story_details(formatted_story_data)
                # Display or use the story_details as needed
                st.write("Story details:", story_details)
            else:
                st.warning("Please complete the character details first.")
