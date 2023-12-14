import streamlit as st
from PIL import Image
from functions import create_tempfile as tf, create_characterdescription as chardesc, generate_image as genimg, update_storydata as sdata
from config import pagesetup as ps

def app_wizard_INI():                                                                                                                             # Initialize story elements form to capture inputs
  with st.form("Initial Story Elements"):                                                                                                                                        # set the details of the form
    ps.set_blue_header("Let's get started! First, please **fill out the fields below.")                                                                                  # Header
    #st.divider()
    uploaded_img = st.file_uploader("Upload a picture of the person/pet you'd like on a card, board, or coloring page", type=['png', 'jpg', 'jpeg', 'gif'])         # Set file uploader to allow user to upload image
    if uploaded_img is not None:                                                                                                                                    # if the user uploads a file then execute condition
      image = Image.open(uploaded_img)                                                                                                                              # open the image using PIL.Image
      image_path = tf.get_tempfile_path(image)                                                                                                                         # get the file path of the temp file or uploaded image
      character_description = chardesc.get_character_description(image_path)                                                                                        # Using the image get a character description from openAI
      character_image = genimg.create_image(character_description)                                                                                                  # Create an image using DALLE3 based on character description
      exp_images = st.expander("View Uploaded and Character Images", expanded = False)                                                                              # create expander to show side by side pictures
      with exp_images:
        cc = st.columns([3,1,3])
        with cc[0]:
          display_image_upload = st.image(image, "Uploaded Image")
        with cc[2]:
          display_image_created = st.image(character_image, "Created Image")
        st.markdown("**Character Description**")
        st.markdown(character_description)
    else:
      st.warning("Please upload at least one image of your loved one.")

    cols_storyelements = st.columns(3)
    with cols_storyelements[0]:
      character_name = st.text_input("Character Name", key="storyelement_charactername")
      genre = st.selectbox("Choose the Genre", key="storyelement_genre", options=["Adventure", "Fairy Tale", "Animal Story", "Space Exploration", "Magical Fantasy", "Surprise Me"])
      supporting_character = st.selectbox("Choose A Supporting Character", key="storyelement_supportingcharacter", options=["Wise Owl", "Funny Clown", "Talking Robot", "Friendly Dragon", "Mischievous Monkey", "Surprise Me"])
      
    with cols_storyelements[1]:
      character_relationship = st.text_input("Relation to Character (e.g. daughter, mother, etc.)", key="storyelement_characterrelation")
      tone = st.selectbox("Choose the Theme", key="storyelement_tone", options=["Joyful", "Exciting", "Mysterious", "Playful", "Heartwarming", "Surprise Me"])
      plot_elements = st.selectbox("Choose Plot Elements", key="storyelement_plotelements", options=["A Hidden Treasure", "A Grand Festival", "A Magic Spell", "A Daring Rescue", "A Secret Door", "Surprise Me"])
      
    with cols_storyelements[2]:
      theme = st.selectbox("Choose the Theme", key="storyelement_theme", options=["Friendship", "Courage", "Kindness", "Discovery", "Teamwork", "Surprise Me"])
      setting = st.selectbox("Choose the Setting", key="storyelement_setting", options=["Enchanted Forest", "Outer Space", "Kingdom", "Under the Sea", "Mystical Mountain", "Surprise Me"])
      magical_objects = st.selectbox("Choose Magical Objects",key="storyelement_magicalobjects", options=["Magic Wand", "Enchanted Mirror", "Golden Key", "Flying Carpet", "Invisible Cloak", "Surprise Me"])

    submit_storyelements = st.form_submit_button("Submit Story Elements and Create MagicBook!")
    if submit_storyelements:
      sdata.update_story_data("character_name", character_name)
      sdata.update_story_data("character_relation", character_relationship)
      sdata.update_story_data("selectedtheme", theme )
      sdata.update_story_data("genre", genre )
      sdata.update_story_data("tonemood", tone)
      sdata.update_story_data("setting", setting)
      sdata.update_story_data("supportingcharacter", supporting_character )
      sdata.update_story_data("plotelements", plot_elements )
      sdata.update_story_data("magicalobjects", magical_objects)
      sdata.update_story_data("character_description", character_description)
      sdata.update_story_data("provided_image_url", character_image)
      st.write("Data Submitted")
      
      
      
    
    
