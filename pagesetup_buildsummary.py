import streamlit as st
from story_data import story_data

# Extracting values from story_data
title = story_data["title"]
summary = story_data["summary"]
provided_image_url = story_data["character"]["provided_image_url"]
character_description = story_data["character"]["character_description"]

# Page 1
page1_narrative = story_data["pages"]["page1"]["narrative"]
page1_imageprompt = story_data["pages"]["page1"]["imageprompt"]
page1_seedid = story_data["pages"]["page1"]["seedid"]
page1_genid = story_data["pages"]["page1"]["genid"]

# Page 2
page2_narrative = story_data["pages"]["page2"]["narrative"]
page2_imageprompt = story_data["pages"]["page2"]["imageprompt"]
page2_seedid = story_data["pages"]["page2"]["seedid"]
page2_genid = story_data["pages"]["page2"]["genid"]

# Page 3
page3_narrative = story_data["pages"]["page3"]["narrative"]
page3_imageprompt = story_data["pages"]["page3"]["imageprompt"]
page3_seedid = story_data["pages"]["page3"]["seedid"]
page3_genid = story_data["pages"]["page3"]["genid"]

# Page 4
page4_narrative = story_data["pages"]["page4"]["narrative"]
page4_imageprompt = story_data["pages"]["page4"]["imageprompt"]
page4_seedid = story_data["pages"]["page4"]["seedid"]
page4_genid = story_data["pages"]["page4"]["genid"]

# Page 5
page5_narrative = story_data["pages"]["page5"]["narrative"]
page5_imageprompt = story_data["pages"]["page5"]["imageprompt"]
page5_seedid = story_data["pages"]["page5"]["seedid"]
page5_genid = story_data["pages"]["page5"]["genid"]

# Page 6
page6_narrative = story_data["pages"]["page6"]["narrative"]
page6_imageprompt = story_data["pages"]["page6"]["imageprompt"]
page6_seedid = story_data["pages"]["page6"]["seedid"]
page6_genid = story_data["pages"]["page6"]["genid"]

# Page 7
page7_narrative = story_data["pages"]["page7"]["narrative"]
page7_imageprompt = story_data["pages"]["page7"]["imageprompt"]
page7_seedid = story_data["pages"]["page7"]["seedid"]
page7_genid = story_data["pages"]["page7"]["genid"]

# Page 8
page8_narrative = story_data["pages"]["page8"]["narrative"]
page8_imageprompt = story_data["pages"]["page8"]["imageprompt"]
page8_seedid = story_data["pages"]["page8"]["seedid"]
page8_genid = story_data["pages"]["page8"]["genid"]

# Page 9
page9_narrative = story_data["pages"]["page9"]["narrative"]
page9_imageprompt = story_data["pages"]["page9"]["imageprompt"]
page9_seedid = story_data["pages"]["page9"]["seedid"]
page9_genid = story_data["pages"]["page9"]["genid"]

# Page 10
page10_narrative = story_data["pages"]["page10"]["narrative"]
page10_imageprompt = story_data["pages"]["page10"]["imageprompt"]
page10_seedid = story_data["pages"]["page10"]["seedid"]
page10_genid = story_data["pages"]["page10"]["genid"]

pagecount = story_data["pagecount"]

def get_buildsummary():
  container0 = st.container(border=True)
  container1 = st.container(border=True)
  container2 = st.container(border=True)
  container3 = st.container(border=True)
  container4 = st.container(border=True)
  container5 = st.container(border=True)
  container6 = st.container(border=True)
  container7 = st.container(border=True)
  container8 = st.container(border=True)
  container9 = st.container(border=True)
  container10 = st.container(border=True)
