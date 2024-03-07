from flask import jsonify
from zipfile import ZipFile
from flask import send_file
import os
from config import APP_PATH

# Define the path to the static/images directory
STATIC_IMAGES_DIR = os.path.join(APP_PATH, 'static', 'images')
ZIP_FOLDER = os.path.join(APP_PATH, 'static', 'zip')


def save_image_local(image):
    save_path = os.path.join(APP_PATH, 'static', 'uploads', 'received.png')
    image.save(save_path)
    return 'Image saved successfully', 200


def create_zip_and_send():
    image_paths = [
        os.path.join(STATIC_IMAGES_DIR, 'a_painting_of_man_waiting_for_hi.png'),
        os.path.join(STATIC_IMAGES_DIR, 'a_painting_of_man_waiting_for_hi_1.png'),
        os.path.join(STATIC_IMAGES_DIR, 'a_painting_of_man_waiting_for_hi_2.png'),
        os.path.join(STATIC_IMAGES_DIR, 'a_painting_of_man_waiting_for_hi_3.png'),
        os.path.join(STATIC_IMAGES_DIR, 'a_painting_of_man_waiting_for_hi_4.png'),
        os.path.join(STATIC_IMAGES_DIR, 'a_painting_of_man_waiting_for_hi_5.png'),
    ]
    print("Here in the dummy_get_images_zip")
    print(image_paths)

    zip_file_path = (os.path.join(ZIP_FOLDER, 'images.zip'))

    try:
        # Check if all image paths exist
        if all(os.path.exists(image_path) for image_path in image_paths):
            # Create a temporary ZIP file
            with ZipFile(zip_file_path, 'w') as zip_file:
                # Add each image to the ZIP file
                for image_path in image_paths:
                    zip_file.write(image_path, os.path.basename(image_path))
            # Return the ZIP file as a response
            return send_file(zip_file_path, mimetype='application/zip',
                             as_attachment=True)
        else:
            # Raise an exception if one or more images are not found
            raise FileNotFoundError("One or more images not found")
    except Exception as e:
        # Handle any exceptions and return an appropriate response
        return f"An error occurred: {str(e)}"


def dummy_get_images_zip():
    image_paths = [
        'images/a_painting_of_man_waiting_for_hi.png',
        'images/a_painting_of_man_waiting_for_hi_1.png',
        'images/a_painting_of_man_waiting_for_hi_2.png',
        'images/a_painting_of_man_waiting_for_hi_3.png',
        'images/a_painting_of_man_waiting_for_hi_4.png',
        'images/a_painting_of_man_waiting_for_hi_5.png',
    ]
    print("Here1")

    print()
    # Check if all images exist
    if all(os.path.exists(image_path) for image_path in image_paths):
        # Create a temporary ZIP file
        with ZipFile('images.zip', 'w') as zip_file:
            # Add each image to the ZIP file
            for image_path in image_paths:
                zip_file.write(image_path, os.path.basename(image_path))
        print("Here2")
        # Return the ZIP file as a response
        return send_file('images.zip', mimetype='application/zip',
                         as_attachment=True)
    else:
        return 'One or more images not found', 404


def create_zip(images):
    """
    Create a ZIP file containing the given images.

    Args:
        images (list): A list of paths to image files.

    Returns:
        str or None: The name of the created ZIP file if successful, None otherwise.
    """
    if all(os.path.exists(image_path) for image_path in images):
        with ZipFile('../images.zip', 'w') as zip_file:
            for image_path in images:
                zip_file.write(image_path, os.path.basename(image_path))
        return 'images.zip'
    else:
        return None



# def your_route_function():
#     """
#     Your Flask route function to handle the request.
#
#     Returns:
#         str or Response: A response indicating success or failure.
#     """
#     zip_file = create_zip(image_paths)
#     if zip_file:
#         return send_file(zip_file, mimetype='application/zip', as_attachment=True)
#     else:
#         return 'One or more images not found', 404
