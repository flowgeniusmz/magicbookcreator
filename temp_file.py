from tempfile import NamedTemporaryFile
import streamlit as st


def get_tempfile_path(varImage):
  with NamedTemporaryFile(delete=False) as tmpfile:
    tmpfile.write(varImage.read())
    image_path = tmpfile.name
    return image_path




