# __init__.py

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
print("stabl_Ai package initialized successfully!")
