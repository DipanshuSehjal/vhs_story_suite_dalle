import base64
import os
import requests

body = {
  "samples": 1,
  "height": 1024,
  "width": 1024,
  "steps": 40,
  "cfg_scale": 5,
  "text_prompts": [
    {
      "text": "A painting of a cat",
      "weight": 1
    },
    {
      "text": "blurry, bad",
      "weight": -1
    }
  ],
}

response = requests.post(
  "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image",
  headers={
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "Bearer YOUR_API_KEY",
  },
  json=body,
)

if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))

data = response.json()

# make sure the out directory exists
if not os.path.exists("./out"):
    os.makedirs("./out")

for i, image in enumerate(data["artifacts"]):
    with open(f'./out/txt2img_{image["seed"]}.png', "wb") as f:
        f.write(base64.b64decode(image["base64"]))