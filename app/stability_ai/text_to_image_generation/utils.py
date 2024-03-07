# stability_ai/text_to_image_generation/utils.py

def extract_text_to_image_parameters(request_data):
    """
    Extract text-to-image generation parameters from the request data.

    Args:
        request_data (dict): The request data containing parameters for text-to-image generation.

    Returns:
        dict: A dictionary containing extracted parameters.
    """
    try:
        steps = request_data.get('steps')
        width = request_data.get('width')
        height = request_data.get('height')
        seed = request_data.get('seed')
        cfg_scale = request_data.get('cfg_scale')
        samples = request_data.get('samples')
        positive_prompt = request_data.get('positivePrompt')
        negative_prompt = request_data.get('negativePrompt')
        count = request_data.get('count')
        style = request_data.get('style')

        # Return the extracted parameters as a dictionary
        return {
            'steps': steps,
            'width': width,
            'height': height,
            'seed': seed,
            'cfg_scale': cfg_scale,
            'samples': samples,
            'positive_prompt': positive_prompt,
            'negative_prompt': negative_prompt,
            'count': count,
            'style': style
        }
    except Exception as e:
        # Log the error or handle it accordingly
        raise Exception("Error extracting text-to-image parameters: " + str(e))
