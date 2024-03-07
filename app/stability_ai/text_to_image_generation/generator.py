# stability_ai.text_to_image_generation.generator.py

import base64
import os
import requests
from app.utilities import create_zip
from app.stability_ai.config import API_KEY, TEXT_TO_IMAGE_API_URL


class TextToImageConfig:
    """
    A class to represent the configuration for text-to-image generation.
    Attributes:
        steps (int): The number of steps for generation.
        width (int): The width of the generated images.
        height (int): The height of the generated images.
        seed (int): The seed for random generation.
        cfg_scale (int): The scale factor for the configuration.
        samples (int): The number of samples to generate.
        positive_prompt (str): The positive text prompt.
        negative_prompt (str): The negative text prompt.
        count (int): The number of images to generate.
        style (str): The style of the generated images.
    """

    def __init__(self, steps=40, width=1024, height=1024, seed=0, cfg_scale=5, samples=1, positive_prompt=None,
                 negative_prompt=None, count=1, style=None):
        """
        Initializes the TextToImageConfig with the provided parameters.
        Parameters:
            steps (int): The number of steps for generation.
            width (int): The width of the generated images.
            height (int): The height of the generated images.
            seed (int): The seed for random generation.
            cfg_scale (int): The scale factor for the configuration.
            samples (int): The number of samples to generate.
            positive_prompt (str): The positive text prompt.
            negative_prompt (str): The negative text prompt.
            count (int): The number of images to generate.
            style (str): The style of the generated images.
        """
        self.samples = samples
        self.height = height
        self.width = width
        self.steps = steps
        self.seed = seed
        self.cfg_scale = cfg_scale
        self.style = style
        self.count = count
        self.positive_prompt = positive_prompt if positive_prompt else "A painting of a cat"
        self.negative_prompt = negative_prompt if negative_prompt else "blurry, bad"
        self.text_prompts = [
            {
                "text": self.positive_prompt,
                "weight": 1
            },
            {
                "text": self.negative_prompt,
                "weight": -1
            }
        ]


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
