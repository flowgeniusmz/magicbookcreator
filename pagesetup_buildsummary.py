import streamlit as st
from story_data import story_data



# Extracting values from story_data
title = story_data["title"]
summary = story_data["summary"]

#character
provided_image_url = story_data["character"]["provided_image_url"]
character_description = story_data["character"]["character_description"]# Extracting values from story_data
lovedonename = story_data["character"]["lovedonename"]
lovedonerelationship = story_data["character"]["lovedonerelationship"]

# storyelements
genre = story_data["storyelements"]["genre"]
setting = story_data["storyelements"]["setting"]
supportingcharacter = story_data["storyelements"]["supportingcharacter"]
plotelements = story_data["storyelements"]["plotelements"]
selectedtheme = story_data["storyelements"]["selectedtheme"]
magicalobjects = story_data["storyelements"]["magicalobjects"]
tonemood = story_data["storyelements"]["tonemood"]


# Page 1
page1_narrative = story_data["pages"]["page1"]["narrative"]
page1_imageprompt = story_data["pages"]["page1"]["imageprompt"]
page1_seedid = story_data["pages"]["page1"]["seedid"]
page1_genid = story_data["pages"]["page1"]["genid"]
page1_imagefile = story_data["pages"]["page1"]["imagefile"]
page1_imageurl = story_data["pages"]["page1"]["imageurl"]

# Page 2
page2_narrative = story_data["pages"]["page2"]["narrative"]
page2_imageprompt = story_data["pages"]["page2"]["imageprompt"]
page2_seedid = story_data["pages"]["page2"]["seedid"]
page2_genid = story_data["pages"]["page2"]["genid"]
page2_imagefile = story_data["pages"]["page2"]["imagefile"]
page2_imageurl = story_data["pages"]["page2"]["imageurl"]

# Page 3
page3_narrative = story_data["pages"]["page3"]["narrative"]
page3_imageprompt = story_data["pages"]["page3"]["imageprompt"]
page3_seedid = story_data["pages"]["page3"]["seedid"]
page3_genid = story_data["pages"]["page3"]["genid"]
page3_imagefile = story_data["pages"]["page3"]["imagefile"]
page3_imageurl = story_data["pages"]["page3"]["imageurl"]

# Page 4
page4_narrative = story_data["pages"]["page4"]["narrative"]
page4_imageprompt = story_data["pages"]["page4"]["imageprompt"]
page4_seedid = story_data["pages"]["page4"]["seedid"]
page4_genid = story_data["pages"]["page4"]["genid"]
page4_imagefile = story_data["pages"]["page4"]["imagefile"]
page4_imageurl = story_data["pages"]["page4"]["imageurl"]

# Page 5
page5_narrative = story_data["pages"]["page5"]["narrative"]
page5_imageprompt = story_data["pages"]["page5"]["imageprompt"]
page5_seedid = story_data["pages"]["page5"]["seedid"]
page5_genid = story_data["pages"]["page5"]["genid"]
page5_imagefile = story_data["pages"]["page5"]["imagefile"]
page5_imageurl = story_data["pages"]["page5"]["imageurl"]

# Page 6
page6_narrative = story_data["pages"]["page6"]["narrative"]
page6_imageprompt = story_data["pages"]["page6"]["imageprompt"]
page6_seedid = story_data["pages"]["page6"]["seedid"]
page6_genid = story_data["pages"]["page6"]["genid"]
page6_imagefile = story_data["pages"]["page6"]["imagefile"]
page6_imageurl = story_data["pages"]["page6"]["imageurl"]

# Page 7
page7_narrative = story_data["pages"]["page7"]["narrative"]
page7_imageprompt = story_data["pages"]["page7"]["imageprompt"]
page7_seedid = story_data["pages"]["page7"]["seedid"]
page7_genid = story_data["pages"]["page7"]["genid"]
page7_imagefile = story_data["pages"]["page7"]["imagefile"]
page7_imageurl = story_data["pages"]["page7"]["imageurl"]

# Page 8
page8_narrative = story_data["pages"]["page8"]["narrative"]
page8_imageprompt = story_data["pages"]["page8"]["imageprompt"]
page8_seedid = story_data["pages"]["page8"]["seedid"]
page8_genid = story_data["pages"]["page8"]["genid"]
page8_imagefile = story_data["pages"]["page8"]["imagefile"]
page8_imageurl = story_data["pages"]["page8"]["imageurl"]

# Page 9
page9_narrative = story_data["pages"]["page9"]["narrative"]
page9_imageprompt = story_data["pages"]["page9"]["imageprompt"]
page9_seedid = story_data["pages"]["page9"]["seedid"]
page9_genid = story_data["pages"]["page9"]["genid"]
page9_imagefile = story_data["pages"]["page9"]["imagefile"]
page9_imageurl = story_data["pages"]["page9"]["imageurl"]

# Page 10
page10_narrative = story_data["pages"]["page10"]["narrative"]
page10_imageprompt = story_data["pages"]["page10"]["imageprompt"]
page10_seedid = story_data["pages"]["page10"]["seedid"]
page10_genid = story_data["pages"]["page10"]["genid"]
page10_imagefile = story_data["pages"]["page10"]["imagefile"]
page10_imageurl = story_data["pages"]["page10"]["imageurl"]

pagecount = story_data["pagecount"]

def get_buildsummary1():

  container0 = st.container()
  with container0:
      st.title(title)
      st.markdown(summary)
  
  # Create containers for each page and organize the expanders
  for i in range(1, 11):
      with st.container():
          with st.columns(2):
              # Create expanders for Narrative and Illustration
              if i % 2 == 1:  # Odd pages: Narrative left, Illustration right
                  with st.expander(f"Page {i} Narrative", expanded=True):
                      st.write(eval(f"page{i}_narrative"))
  
                  with st.expander(f"Page {i} Illustration", expanded=True):
                      st.image(eval(f"page{i}_imagefile"))
              else:  # Even pages: Illustration left, Narrative right
                  with st.expander(f"Page {i} Illustration", expanded=True):
                      st.image(eval(f"page{i}_imagefile"))
  
                  with st.expander(f"Page {i} Narrative", expanded=True):
                      st.write(eval(f"page{i}_narrative"))



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
