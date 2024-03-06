import base64
import os
import requests
from app.utilities import create_zip
from zipfile import ZipFile
from flask import send_file
from app.stability_ai import API_KEY, TEXT_TO_IMAGE_API_URL


class TextToImageGenerator:
    """
    A class to generate images from text prompts using the Stability AI API.

    Attributes:
        api_key (str): The API key for accessing the Stability AI API.
        base_url (str): The base URL for the API endpoint.
        headers (dict): The headers to be included in the HTTP request.
        body (dict): The default request body containing the text prompts and configuration.
    """

    def __init__(self, config):

        """
        Initializes the TextToImageGenerator with the provided API key.

        Parameters:
            api_key (str): The API key for accessing the Stability AI API.
        """
        self.api_key = API_KEY
        self.base_url = TEXT_TO_IMAGE_API_URL
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }
        self.config = config

    def generate_images(self, count=0):
        """
        Generates images from text prompts using the Stability AI API.
        """
        for c in range(count):
            response = requests.post(self.base_url, headers=self.headers, json=self.config)
            if response.status_code != 200:
                raise Exception("Non-200 response: " + str(response.text))
            data = response.json()
            self.save_images(data)

        return True

    def dummy_get_images_zip(self):
        image_paths = [
            'images/a_painting_of_man_waiting_for_hi.png',
            'images/a_painting_of_man_waiting_for_hi_1.png',
            'images/a_painting_of_man_waiting_for_hi_2.png',
            'images/a_painting_of_man_waiting_for_hi_3.png',
            'images/a_painting_of_man_waiting_for_hi_4.png',
            'images/a_painting_of_man_waiting_for_hi_5.png',
        ]
        print("Here1")
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

    def get_images_as_zip(self, folder_path=None):
        """
        Get images from a folder and return them as a ZIP file.

        Args:
            folder_path (str): Path to the folder containing images.

        Returns:
            str or None: The name of the created ZIP file if successful, None otherwise.
        """
        # Check if the folder exists
        if folder_path and not os.path.exists(folder_path) or not os.path.isdir(folder_path):
            return None

        if not folder_path:
            folder_path = "../../static/images"

        # Get a list of image files in the folder
        image_files = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if
                       os.path.isfile(os.path.join(folder_path, filename)) and
                       filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

        # Check if any image files were found
        if not image_files:
            return None

        # Use the create_zip function to create the ZIP file
        return create_zip(image_files)

    def save_images(self, data):
        """
        Saves the generated images to the 'out' directory.

        Parameters:
            data (dict): The response data containing the generated images.
        """
        # Make sure the 'out' directory exists
        if not os.path.exists("./out"):
            os.makedirs("./out")
        for i, image in enumerate(data["artifacts"]):
            with open(f'./out/txt2img_{image["seed"]}.png', "wb") as f:
                f.write(base64.b64decode(image["base64"]))

    def send_images(self):
        # TODO: add create_zip function
        image_paths = [
            'images/a_painting_of_man_waiting_for_hi.png',
            'images/a_painting_of_man_waiting_for_hi_1.png',
            'images/a_painting_of_man_waiting_for_hi_2.png',
            'images/a_painting_of_man_waiting_for_hi_3.png',
            'images/a_painting_of_man_waiting_for_hi_4.png',
            'images/a_painting_of_man_waiting_for_hi_5.png',
        ]


# # Example usage:
# config = ImageGenerationConfig(
#     samples=1,
#     height=1024,
#     width=1024,
#     steps=40,
#     cfg_scale=5,
#     text_prompts=[
#         {"text": "A painting of a cat", "weight": 1},
#         {"text": "blurry, bad", "weight": -1}
#     ]
# )
# generator = TextToImageGenerator(config=config)
# generator.generate_images()
