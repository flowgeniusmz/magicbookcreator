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

  # Create containers for each page and organize the expanders
  with container0:
      st.title(title)
      st.markdown(summary)
  
  with container1:
      cc1 = st.columns(2)
      with cc1[0]:
          with st.expander("Page 1 Narrative", expanded=True):
              st.write(page1_narrative)
      with cc1[1]:
          with st.expander("Page 1 Illustration", expanded=True):
              st.image(page1_imagefile)
  
  with container2:
      cc2 = st.columns(2)
      with cc2[0]:
          with st.expander("Page 2 Illustration", expanded=True):
              st.image(page2_imagefile)
      with cc2[1]:
          with st.expander("Page 2 Narrative", expanded=True):
              st.write(page2_narrative)
  
  with container3:
      cc3 = st.columns(2)
      with cc3[0]:
          with st.expander("Page 3 Narrative", expanded=True):
              st.write(page3_narrative)
      with cc3[1]:
          with st.expander("Page 3 Illustration", expanded=True):
              st.image(page3_imagefile)
  
  with container4:
      cc4 = st.columns(2)
      with cc4[0]:
          with st.expander("Page 4 Illustration", expanded=True):
              st.image(page4_imagefile)
      with cc4[1]:
          with st.expander("Page 4 Narrative", expanded=True):
              st.write(page4_narrative)
  
  with container5:
      cc5 = st.columns(2)
      with cc5[0]:
          with st.expander("Page 5 Narrative", expanded=True):
              st.write(page5_narrative)
      with cc5[1]:
          with st.expander("Page 5 Illustration", expanded=True):
              st.image(page5_imagefile)
  
  with container6:
      cc6 = st.columns(2)
      with cc6[0]:
          with st.expander("Page 6 Illustration", expanded=True):
              st.image(page6_imagefile)
      with cc6[1]:
          with st.expander("Page 6 Narrative", expanded=True):
              st.write(page6_narrative)
  
  with container7:
      cc7 = st.columns(2)
      with cc7[0]:
          with st.expander("Page 7 Narrative", expanded=True):
              st.write(page7_narrative)
      with cc7[1]:
          with st.expander("Page 7 Illustration", expanded=True):
              st.image(page7_imagefile)
  
  with container8:
      cc8 = st.columns(2)
      with cc8[0]:
          with st.expander("Page 8 Illustration", expanded=True):
              st.image(page8_imagefile)
      with cc8[1]:
          with st.expander("Page 8 Narrative", expanded=True):
              st.write(page8_narrative)
  
  with container9:
      cc9 = st.columns(2)
      with cc9[0]:
          with st.expander("Page 9 Narrative", expanded=True):
              st.write(page9_narrative)
      with cc9[1]:
          with st.expander("Page 9 Illustration", expanded=True):
              st.image(page9_imagefile)
  
  with container10:
      cc10 = st.columns(2)
      with cc10[0]:
          with st.expander("Page 10 Illustration", expanded=True):
              st.image(page10_imagefile)
      with cc10[1]:
          with st.expander("Page 10 Narrative", expanded=True):
              st.write(page10_narrative)

