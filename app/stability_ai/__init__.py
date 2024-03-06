# __init__.py
from .image_generation_config import ImageGenerationConfig
# from .text_to_image import TextToImageGenerator
# from .image_to_image import ImageToImageGenerator

API_KEY = ""

# Define a constant variable for the URL
TEXT_TO_IMAGE_API_URL = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
IMAGE_UPSCALING_API_URL = "https://api.stability.ai/v1/generation/esrgan-v1-x2plus/image-to-image/upscale"
IMAGE_TO_IMAGE_API_URL = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/image-to-image"
MULTI_PROMPTING_API_URL = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

# Optionally, you can include package-level documentation
__doc__ = """
This is the documentation for the stabl_Ai package.
"""

# Initialization code (if needed)
print("stable_AI package initialized successfully!")

