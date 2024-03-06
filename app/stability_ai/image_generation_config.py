class ImageGenerationConfig:
  """
  A class to represent the configuration for image generation.
  Attributes:
      samples (int): The number of samples to generate.
      height (int): The height of the generated images.
      width (int): The width of the generated images.
      steps (int): The number of steps for generation.
      cfg_scale (int): The scale factor for the configuration.
      text_prompts (list): A list of dictionaries representing text prompts and weights.
  """

  def __init__(self, samples=1, height=1024, width=1024, seed=0, steps=40, cfg_scale=5, positive_prompt=None,
               negative_prompt=None, style=None, image=None):
    """
    Initializes the ImageGenerationConfig with the provided parameters.
    Parameters:
        samples (int): The number of samples to generate.
        height (int): The height of the generated images.
        width (int): The width of the generated images.
        steps (int): The number of steps for generation.
        cfg_scale (int): The scale factor for the configuration.
        text_prompts (list): A list of dictionaries representing text prompts and weights.
        e.g.     self.text_prompts = [
                                    {
                                      "text": "A painting of a cat",
                                      "weight": 1
                                    },
                                    {
                                      "text": "blurry, bad",
                                      "weight": -1
                                    }
                                  ]
    """
    self.samples = samples
    self.height = height
    self.width = width
    self.steps = steps
    self.seed = seed
    self.cfg_scale = cfg_scale
    self.style = style
    self.image = image
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
