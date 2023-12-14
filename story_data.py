import streamlit as st


story_data = {
    "title": "",
    "summary": "",
    "character": {
        "provided_image_url": "",
        "character_description": "",
        "lovedonename": "",
        "lovedonerelationship": ""
    },
    "storyelements": {
        "genre": "",
        "setting": "",
        "supportingcharacter": "",
        "plotelements": "",
        "selectedtheme": "",
        "magicalobjects": "",
        "tonemood": ""
    },
    "pages": {
        "page1": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": "",
            "imagefile": "",
            "imageurl": ""
        },
        "page2": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": "",
            "imagefile": "",
            "imageurl": ""
        },
        "page3": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": "",
            "imagefile": "",
            "imageurl": ""
        },
        "page4": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": "",
            "imagefile": "",
            "imageurl": ""
        },
        "page5": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": "",
            "imagefile": "",
            "imageurl": ""
        },
        "page6": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": "",
            "imagefile": "",
            "imageurl": ""
        },
        "page7": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": "",
            "imagefile": "",
            "imageurl": ""
        },
        "page8": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": "",
            "imagefile": "",
            "imageurl": ""
        },
        "page9": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": "",
            "imagefile": "",
            "imageurl": ""
        },
        "page10": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": "",
            "imagefile": "",
            "imageurl": ""
        }
    }
}





def update_story_data(key, value):
    """
    Update the story_data JSON with the provided key and value.
    
    Args:
        key (str): The key where the value should be updated.
        value: The value to update.
    """
    if key in story_data:
        story_data[key] = value
    else:
        print(f"Key '{key}' not found in story_data JSON.")
