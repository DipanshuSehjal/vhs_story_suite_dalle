import torch
from PIL import Image
import numpy as np


from min_dalle import MinDalle

model = MinDalle(
    models_root='./pretrained',
    dtype=torch.float32,
    #device='cuda',
    device='cpu',
    is_mega=True,
    is_reusable=True
)

image = model.generate_image(
    text='Nuclear explosion broccoli',
    seed=-1,
    grid_size=4,
    is_seamless=False,
    temperature=1,
    top_k=256,
    supercondition_factor=32,
    is_verbose=False
)

# Convert the image array to a Pillow Image object
image_pil = Image.fromarray(np.uint8(image))

# Display the image in a GUI window
image_pil.show()
