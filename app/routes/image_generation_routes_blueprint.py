# image_generation_routes_blueprint.py
"""
routes/image_generation_routes_blueprint.py

This module defines routes related to image generation.
"""

from flask import Blueprint, request, jsonify, current_app
from zipfile import ZipFile
from flask import send_file
import os

from config import APP_PATH


# Create a Blueprint object for image generation routes
image_generation_routes = Blueprint('image_generation', __name__)


# Define the route function for /api/text-to-image endpoint
@image_generation_routes.route('/api/text-to-image', methods=['POST'])
def text_to_image_handler():
    """
    Handle POST request for text-to-image generation.

    This route expects JSON data containing parameters for image generation.

    Returns:
        JSON: A response containing image data or error message.
    """
    try:
        data = request.json  # Get JSON data from the request
        # parameters = extract_validate_image_generation_parameters(data)

        # Create a Config instance with the extracted parameters
        # config = ImageGenerationConfig(**parameters)
        # config = ImageGenerationConfig(
        #     steps=parameters.steps,
        #     width=parameters.width,
        #     height=parameters.height,
        #     seed=parameters.seed,
        #     cfg_scale=parameters.cfg_scale,
        #     samples=parameters.samples,
        #     positive_prompt=parameters.positive_prompt,
        #     negative_prompt=parameters.negative_prompt,
        #     style=parameters.style
        # )
        # Extract parameters from the JSON data
        steps = data.get('steps')
        width = data.get('width')
        height = data.get('height')
        seed = data.get('seed')
        cfg_scale = data.get('cfg_scale')
        samples = data.get('samples')
        positive_prompt = data.get('positivePrompt')
        negative_prompt = data.get('negativePrompt')

        # Custom parameters
        count = data.get('count')
        style = data.get('style')
        # Print the extracted parameters
        print("steps:", steps)
        print("width:", width)
        print("height:", height)
        print("seed:", seed)
        print("cfg_scale:", cfg_scale)
        print("samples:", samples)
        print("positive_prompt:", positive_prompt)
        print("negative_prompt:", negative_prompt)
        print("count:", count)

        # config = ImageGenerationConfig(
        #     steps=steps,
        #     width=width,
        #     height=height,
        #     seed=seed,
        #     cfg_scale=cfg_scale,
        #     samples=samples,
        #     positive_prompt=positive_prompt,
        #     negative_prompt=negative_prompt,
        #     style=style
        # )

        # Create a TextToImageGenerator instance with the config
        # generator = TextToImageGenerator(config=config)

        # Call the generate_images method
        # image = generator.generate_images()

        # image is boolean for the time being
        #        if not image:
        #            raise Exception
        # Return the processed data as JSON response
        # This is base64 image

        return create_zip_and_send(), 200

    # return generator.dummy_get_images_zip(), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Internal Server Error


# Define the path to the static/images directory
STATIC_IMAGES_DIR = os.path.join(APP_PATH, 'static', 'images')
ZIP_FOLDER = os.path.join(APP_PATH, 'static', 'zip')

def create_zip_and_send():
    image_paths = [
        os.path.join(STATIC_IMAGES_DIR, 'a_painting_of_man_waiting_for_hi.png'),
        os.path.join(STATIC_IMAGES_DIR, 'a_painting_of_man_waiting_for_hi_1.png'),
        os.path.join(STATIC_IMAGES_DIR, 'a_painting_of_man_waiting_for_hi_2.png'),
        os.path.join(STATIC_IMAGES_DIR, 'a_painting_of_man_waiting_for_hi_3.png'),
        os.path.join(STATIC_IMAGES_DIR, 'a_painting_of_man_waiting_for_hi_4.png'),
        os.path.join(STATIC_IMAGES_DIR, 'a_painting_of_man_waiting_for_hi_5.png'),
        # 'images/a_painting_of_man_waiting_for_hi_1.png',
        # 'images/a_painting_of_man_waiting_for_hi_2.png',
        # 'images/a_painting_of_man_waiting_for_hi_3.png',
        # 'images/a_painting_of_man_waiting_for_hi_4.png',
        # 'images/a_painting_of_man_waiting_for_hi_5.png',
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


@image_generation_routes.route('/api/image-to-image', methods=['POST'])
def image_to_image_handler():
    """
    Handle POST request to upload a file.

    This route expects form data containing fields for image generation parameters
    along with an uploaded image file.

    Returns:
        str: A message indicating the success of the file upload.
    """
    try:
        # Access form fields
        print("request.form is: ", request.form)
        steps = request.form.get('steps')
        width = request.form.get('width')
        height = request.form.get('height')
        seed = request.form.get('seed')
        cfg_scale = request.form.get('cfg_scale')
        samples = request.form.get('samples')
        positive_prompt = request.form.get('positivePrompt')
        negative_prompt = request.form.get('negativePrompt')
        count = request.form.get('count')
        style = request.form.get('style')
        # Access uploaded file
        upload_image = request.files['uploadImage']


        # Print the extracted parameters
        print("steps:", steps)
        print("width:", width)
        print("height:", height)
        print("seed:", seed)
        print("cfg_scale:", cfg_scale)
        print("samples:", samples)
        print("positive_prompt:", positive_prompt)
        print("negative_prompt:", negative_prompt)
        print("count:", count)
        print("style:", style)

        # config = ImageGenerationConfig(
        #     steps=steps,
        #     width=width,
        #     height=height,
        #     seed=seed,
        #     cfg_scale=cfg_scale,
        #     samples=samples,
        #     positive_prompt=positive_prompt,
        #     negative_prompt=negative_prompt,
        #     style=style
        # )
        #
        # # Create a TextToImageGenerator instance with the config
        # generator = ImageToImageGenerator(config=config)

        # Call the generate_images method
        # image = generator.generate_images()

        # image is boolean for the time being
        #        if not image:
        #            raise Exception
        # Return the processed data as JSON response
        # This is base64 image

        # Specify the filename where you want to save the image

        # BIG ALERT. MY FILE NAME RECEIVED FROM FRONTEND SERVER IS NOT WORKING


        # CULPRIT BIG CULPRIT
        # filename = 'received_image.png'
        # save_image_to_print(image, filename)
        # print(f"Image saved as {filename}")
        # CULPRIT BIG CULPRIT

        print("printing image: ")

        #return generator.dummy_get_images_zip(), 200
        return create_zip_and_send(), 200

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500  # Internal Server Error