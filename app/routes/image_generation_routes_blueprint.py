# image_generation_routes_blueprint.py
"""
routes/image_generation_routes_blueprint.py

This module defines routes related to image generation.
"""

from flask import Blueprint, request, jsonify, current_app
import app.utilities as app_utils
from app.stability_ai import TextToImageConfig, TextToImageGenerator, ImageToImageConfig, ImageToImageGenerator
from app.stability_ai import t_2_i_utils, i_2_i_utils


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

        # Extract parameters using the utility function
        parameters = t_2_i_utils.extract_text_to_image_parameters(data)
        print(parameters)

        # Create a Config instance with the extracted parameters
        config = TextToImageConfig(**parameters)
        print("config")

        # Create a TextToImageGenerator instance with the config
        generator = TextToImageGenerator(config=config)

        # Call the generate_images method
        # image = generator.generate_images()

        # image is boolean for the time being
        #        if not image:
        #            raise Exception
        # Return the processed data as JSON response
        # This is base64 image

        return app_utils.create_zip_and_send(), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Internal Server Error


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
        # Extract parameters using the utility function

        parameters = i_2_i_utils.extract_image_to_image_parameters(request)
        print(parameters)

        # Create a Config instance with the extracted parameters
        config = ImageToImageConfig(**parameters)
        print("config")

        # Create a ImageToImageGenerator instance with the config
        generator = ImageToImageGenerator(config=config)

        # Call the generate_images method
        # image = generator.generate_images()

        # image is boolean for the time being
        #        if not image:
        #            raise Exception
        # Return the processed data as JSON response
        # This is base64 image

        # Specify the filename where you want to save the image

        #return generator.dummy_get_images_zip(), 200
        app_utils.save_image_local(config.upload_image)
        return app_utils.create_zip_and_send(), 200

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500  # Internal Server Error