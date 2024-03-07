# stability_ai/image_to_image_generation/generator.py
import base64
import os

from app.stability_ai.config import API_KEY, IMAGE_TO_IMAGE_API_URL
import requests


class ImageToImageConfig:
    """
    A class to represent the configuration for image-to-image generation.

    Attributes:
        steps (str): The number of steps for generation.
        width (str): The width of the generated images.
        height (str): The height of the generated images.
        seed (str): The seed for random generation.
        cfg_scale (str): The scale factor for the configuration.
        samples (str): The number of samples to generate.
        positive_prompt (str): The positive text prompt.
        negative_prompt (str): The negative text prompt.
        count (str): The number of images to generate.
        style (str): The style of the generated images.
        upload_image (FileStorage): The uploaded image file.
    """

    def __init__(self, steps=40, width=1024, height=1024, seed=0, cfg_scale=5, samples=1, positive_prompt=None,
                 negative_prompt=None, count=1, style=None, upload_image=None):
        """
        Initializes the ImageToImageConfig with the provided parameters.

        Parameters:
            steps (str): The number of steps for generation.
            width (str): The width of the generated images.
            height (str): The height of the generated images.
            seed (str): The seed for random generation.
            cfg_scale (str): The scale factor for the configuration.
            samples (str): The number of samples to generate.
            positive_prompt (str): The positive text prompt.
            negative_prompt (str): The negative text prompt.
            count (str): The number of images to generate.
            style (str): The style of the generated images.
            upload_image (FileStorage): The uploaded image file.
        """
        self.steps = steps
        self.width = width
        self.height = height
        self.seed = seed
        self.cfg_scale = cfg_scale
        self.samples = samples
        self.count = count
        self.style = style
        self.upload_image = upload_image
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


class ImageToImageGenerator:
    """
    A class to generate images from image and text prompts using the Stability AI API.

    Attributes:
        api_key (str): The API key for accessing the Stability AI API.
        base_url (str): The base URL for the API endpoint.
        headers (dict): The headers to be included in the HTTP request.
        body (dict): The default request body containing the text prompts and configuration.
    """

    def __init__(self, config):

        """
        Initializes the ImageToImageGenerator with the provided API key.

        Parameters:
            api_key (str): The API key for accessing the Stability AI API.
        """
        self.api_key = API_KEY
        self.base_url = IMAGE_TO_IMAGE_API_URL
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

