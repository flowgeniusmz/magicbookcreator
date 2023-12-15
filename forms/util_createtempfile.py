from PIL import Image
import tempfile

def create_temp_file_for_uploaded_image(uploaded_image):
    """
    Create a temporary file for the uploaded image and return its file path.

    :param uploaded_image: The uploaded image file
    :return: Path of the temporary file
    """
    if uploaded_image is not None:
        # Open the uploaded image using PIL
        image = Image.open(uploaded_image)

        # Create a temporary file and save the uploaded image
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp_file:
            image.save(tmp_file, format='PNG')
            tmp_file_path = tmp_file.name

        return tmp_file_path
    else:
        return None
