import streamlit as st

def create_input_field(input_type, label, options=None):
    """
    Create a dynamic input field based on the specified type with automatic key generation
    and a standard help text mentioning the field name.

    :param input_type: 'text' for text_input or 'select' for selectbox
    :param label: Display label for the widget
    :param options: List of options for selectbox (required if input_type is 'select')
    :return: The created widget
    """
    key = label.lower().replace(" ", "")
    help_text = f"Enter or select the {label.lower()} for the story."

    if input_type == 'text':
        return st.text_input(label=label, key=key, help=help_text)
    elif input_type == 'select' and options is not None:
        return st.selectbox(label=label, key=key, options=options, help=help_text)
    else:
        raise ValueError("Invalid input type or missing options for selectbox")
