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
    text='living room with white walls and white false ceiling with yellow hanging lights. There is a sofa set in the center',
    seed=2,
    grid_size=2,
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
