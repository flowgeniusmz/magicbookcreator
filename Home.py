import streamlit as st
import openai
from openai import OpenAI
from PIL import Image
from character_description import get_character_description
from temp_file import get_tempfile_path
from generate_image import create_image
from story_data import update_story_data
from apps import wizard_INI as wINI
from config import sessionstates as ss

# 0. Set page config
st.set_page_config(page_title = "MagicBook Creator", page_icon = "📚", layout = "wide", initial_sidebar_state = "collapsed")
ss.initialize_session_states()

st.title('Storybook Creator')
st.markdown("Welcome to the story book creator, a place where AI technology can make any person on the planet the main character! Don't believe me? Give it a shot for yourself!")
"---"
tab_INI, tab_AI, tab_BS, tab_DS = st.tabs(["Initial Story Elements", "AI Story Builder", "Build Summary", "Download Story"])

with tab_INI:
    with st.form('Story elements Form'):
        st.markdown("Let's get started, please fill out the following fields:")
        'upload a pciture of a loved one here:'
        uploaded_img = st.file_uploader("Upload a picture of the person/pet you'd like on a card, board, or coloring page", type=['png', 'jpg', 'jpeg', 'gif'])
        if uploaded_img is not None:
            image = Image.open(uploaded_img)                                                                            # Set the uploaded image to an object
            image_path = get_tempfile_path(image)                                                                       # Call 'get_tempfile_path' function to create a temp file for the image uploaded
            characterdescription = get_character_description(image_path)                                                # Call the 'get_character_description" function using the image path (OPENAIVISION)
            character_image = create_image(characterdescription)                                                        # Call the 'create_image' function using characterdescription (OPENAI DALLE3)
            exp_character = st.expander("View Character Image and Description", expanded = False)                       # Display the image and character description in expander
            with exp_character:
                display_image = st.image(character_image, characterdescription)                                         # Display the image created
                st.markdown(f"""{characterdescription}""")                                                              # Display the character description
            
        else:
            st.warning('Please upload at least one image of your loved one')
        lmnt_cols = st.columns(2)
        with lmnt_cols[0]:
            name_of_loved = st.text_input('Name of loved one')
            genre = st.selectbox(
                "Choose the Genre:",
                options=["Adventure", "Fairy Tale", "Animal Story", "Space Exploration", "Magical Fantasy", "surprise me"]
            )
            supporting_character = st.selectbox(
                "Choose A Supporting Character:",
                options=["Wise Owl", "Funny Clown", "Talking Robot", "Friendly Dragon", "Mischievous Monkey", "surprise me"],
            )
            theme = st.selectbox(
                "Choose the Theme:",
                options=["Friendship", "Courage", "Kindness", "Discovery", "Teamwork", "surprise me"]
            )
            tone = st.selectbox(
                "Choose the Tone/Mood:",
                options=["Joyful", "Exciting", "Mysterious", "Playful", "Heartwarming", "surprise me"]
            )
        with lmnt_cols[1]:
            relation = st.text_input('Relation to loved one')
            setting = st.selectbox(
                "Choose the Setting:",
                options=["Enchanted Forest", "Outer Space", "Kingdom", "Under the Sea", "Mystical Mountain", "surprise me"]
            )
            plot_elements = st.selectbox(
                "Choose Plot Elements:",
                options=["A Hidden Treasure", "A Grand Festival", "A Magic Spell", "A Daring Rescue", "A Secret Door", "surprise me"]
            )
            magical_objects = st.selectbox(
                "Choose Magical Objects:",
                options=["Magic Wand", "Enchanted Mirror", "Golden Key", "Flying Carpet", "Invisible Cloak", "surprise me"]
            )

        submitted_elements = st.form_submit_button('Pull Initial Elements')
        # Will need to update this data dump instead to an ai
        if submitted_elements:
            st.success("We've collected and submitted the information you provided, pop over to the next tab (AI Story builder) to see the AI at work!")
            with tab_AI:
                st.write(f"I'd like you to create a story about my {relation}, {name_of_loved}. The story's Genre will be: {genre}, with a setting as: {setting}. A supporting character will be: {supporting_character}, with a plot element of: {plot_elements}. The theme of the story is: {theme}, a magical object, included somewhere in the story is a: {magical_objects}, and the tone will be: {tone} ")
                st.image  # You should specify the image to display here

with tab_AI:
    wINI.app_wizard_INI()
    
    
with tab_BS:
    
    container0 = st.container(border=True)
    with container0: 
        st.title('Title Placeholder')
        st.markdown('Summary Placeholder')
        
    container1 = st.container(border=True)
    with container1: 
        cc1 = st.columns([3,1,3])
        with cc1[0]:
            exp11 = st.expander("Page 1 Narrative", expanded = True)
            with exp11: 
                st.markdown("Narrative")
        with cc1[2]: 
            exp12 = st.expander("Page 1 Illustration", expanded = True)
            with exp12:
                st.markdown("Illustration")
        
    container2 = st.container(border=True)
    with container2: 
        cc2 = st.columns([3,1,3])
        with cc2[0]:
            exp21 = st.expander("Page 2 Illustration", expanded = True)
            with exp21:
                st.markdown("Illustration")
                
        with cc2[2]: 
            exp22 = st.expander("Page 2 Narrative", expanded = True)
            with exp22: 
                st.markdown("Narrative")
        
    container3 = st.container(border=True)
    with container3: 
        cc3 = st.columns([3,1,3])
        with cc3[0]:
            exp31 = st.expander("Page 3 Narrative", expanded = True)
            with exp31: 
                st.markdown("Narrative")
        with cc3[2]: 
            exp32 = st.expander("Page 3 Illustration", expanded = True)
            with exp32:
                st.markdown("Illustration")
            
    container4 = st.container(border=True)
    with container4: 
        cc4 = st.columns([3,1,3])
        with cc4[0]:
            exp41 = st.expander("Page 4 Illustration", expanded = True)
            with exp41:
                st.markdown("Illustration")
                
        with cc4[2]: 
            exp42 = st.expander("Page 4 Narrative", expanded = True)
            with exp42: 
                st.markdown("Narrative")
            
    container5 = st.container(border=True)
    with container5: 
        cc5 = st.columns([3,1,3])
        with cc5[0]:
            exp51 = st.expander("Page 5 Narrative", expanded = True)
            with exp51: 
                st.markdown("Narrative")
                
        with cc5[2]: 
            exp52 = st.expander("Page 5 Illustration", expanded = True)
            with exp52:
                st.markdown("Illustration")
            
    container6 = st.container(border=True)
    with container6: 
        cc6 = st.columns([3,1,3])
        with cc6[0]:
            exp61 = st.expander("Page 6 Illustration", expanded = True)
            with exp61:
                st.markdown("Illustration")
                
        with cc6[2]: 
            exp62 = st.expander("Page 6 Narrative", expanded = True)
            with exp62: 
                st.markdown("Narrative")
            
    container7 = st.container(border=True)
    with container7: 
        cc7 = st.columns([3,1,3])
        with cc7[0]:
            exp71 = st.expander("Page 7 Narrative", expanded = True)
            with exp71: 
                st.markdown("Narrative")
                
        with cc7[2]: 
            exp72 = st.expander("Page 7 Illustration", expanded = True)
            with exp72:
                st.markdown("Illustration")
            
    container8 = st.container(border=True)
    with container8: 
        cc8 = st.columns([3,1,3])
        with cc8[0]:
            exp81 = st.expander("Page 8 Illustration", expanded = True)
            with exp81:
                st.markdown("Illustration")
                
        with cc8[2]: 
            exp82 = st.expander("Page 8 Narrative", expanded = True)
            with exp82: 
                st.markdown("Narrative")
            
    container9 = st.container(border=True)
    with container9: 
        cc9 = st.columns([3,1,3])
        with cc9[0]:
            exp91 = st.expander("Page 9 Narrative", expanded = True)
            with exp91: 
                st.markdown("Narrative")
                
        with cc9[2]: 
            exp92 = st.expander("Page 9 Illustration", expanded = True)
            with exp92:
                st.markdown("Illustration")
            
    container10 = st.container(border=True)
    with container10: 
        cc10 = st.columns([3,1,3])
        with cc10[0]:
            exp101 = st.expander("Page 10 Illustration", expanded = True)
            with exp101:
                st.markdown("Illustration")
                
        with cc10[2]: 
            exp102 = st.expander("Page 10 Narrative", expanded = True)
            with exp102: 
                st.markdown("Narrative")
    

    st.write("Your storybook's narrative and pages in order:")

    st.button("Finalize the story")
