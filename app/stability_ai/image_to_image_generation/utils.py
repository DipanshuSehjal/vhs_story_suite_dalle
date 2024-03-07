# stability_ai/image_to_image_generation/utils.py

def extract_image_to_image_parameters(request):
    """
    Extracts parameters for image-to-image generation from the request.

    Parameters:
        request (flask.Request): The request object containing form data.

    Returns:
        dict: A dictionary containing the extracted parameters.
    """
    try:
        # Access form fields
        steps = request.form.get('steps')
        width = request.form.get('width')
        height = request.form.get('height')
        seed = request.form.get('seed')
        cfg_scale = request.form.get('cfg_scale')
        samples = request.form.get('samples')
        positive_prompt = request.form.get('positivePrompt')
        negative_prompt = request.form.get('negativePrompt')
        count = request.form.get('count')
        style = request.form.get('style')
        # Access uploaded file
        upload_image = request.files['uploadImage']

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
            'style': style,
            'upload_image': upload_image
        }
    except Exception as e:
        # Handle any exceptions and return None
        print("Error extracting parameters:", e)
        return None
