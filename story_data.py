import streamlit as st


story_data = {
    "title": "",
    "summary": "",
    "character": {
        "provided_image_url": "",
        "character_description": ""
    },
    "pages": {
        "page1": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": ""
        },
        "page2": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": ""
        },
        "page3": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": ""
        },
        "page4": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": ""
        },
        "page5": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": ""
        },
        "page6": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": ""
        },
        "page7": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": ""
        },
        "page8": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": ""
        },
        "page9": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": ""
        },
        "page10": {
            "narrative": "",
            "imageprompt": "",
            "seedid": "",
            "genid": ""
        }
    },
    "pagecount": 0
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
