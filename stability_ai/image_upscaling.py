import base64
import os
import requests

response = requests.post(
    "https://api.stability.ai/v1/generation/esrgan-v1-x2plus/image-to-image/upscale",
    headers={
        "Accept": "application/json",
        "Authorization": f"Bearer YOUR_API_KEY"
    },
    files={
        "image": open("../init_image.png", "rb")
    },
    data={
        "height": 0
    }
)

if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))

data = response.json()

# make sure the out directory exists
if not os.path.exists("./out"):
    os.makedirs("./out")

for i, image in enumerate(data["artifacts"]):
    with open(f'./out/upscale_{image["seed"]}.png', "wb") as f:
        f.write(base64.b64decode(image["base64"]))