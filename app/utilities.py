from flask import jsonify
from zipfile import ZipFile
from flask import send_file
import os


def dummy_get_images_zip():
    image_paths = [
        'images/a_painting_of_man_waiting_for_hi.png',
        'images/a_painting_of_man_waiting_for_hi_1.png',
        'images/a_painting_of_man_waiting_for_hi_2.png',
        'images/a_painting_of_man_waiting_for_hi_3.png',
        'images/a_painting_of_man_waiting_for_hi_4.png',
        'images/a_painting_of_man_waiting_for_hi_5.png',
    ]
    print("Here1")

    print()
    # Check if all images exist
    if all(os.path.exists(image_path) for image_path in image_paths):
        # Create a temporary ZIP file
        with ZipFile('images.zip', 'w') as zip_file:
            # Add each image to the ZIP file
            for image_path in image_paths:
                zip_file.write(image_path, os.path.basename(image_path))
        print("Here2")
        # Return the ZIP file as a response
        return send_file('images.zip', mimetype='application/zip',
                         as_attachment=True)
    else:
        return 'One or more images not found', 404


def extract_validate_image_generation_parameters(data):
    # Get JSON data from the request
    # Check if JSON data is present
    if not data:
        return jsonify({'error': 'No JSON data provided'}), 400

    # Extract parameters from the JSON data
    steps = data.get('steps')
    width = data.get('width')
    height = data.get('height')
    seed = data.get('seed')
    cfg_scale = data.get('cfg_scale')
    samples = data.get('samples')
    positive_prompt = data.get('positivePrompt')
    negative_prompt = data.get('negativePrompt')

    # Custom parameters
    count = data.get('count')
    style = data.get('style')


    # # Print the extracted parameters
    # print("steps:", steps)
    # print("width:", width)
    # print("height:", height)
    # print("seed:", seed)
    # print("cfg_scale:", cfg_scale)
    # print("samples:", samples)
    # print("positive_prompt:", positive_prompt)
    # print("negative_prompt:", negative_prompt)
    # print("count:", count)
    #
    #
    #
    # print("here")
    # # Check if required parameters are present
    # if None in [steps, width, height, seed, cfg_scale, samples, positive_prompt, negative_prompt]:
    #     raise ValueError('Missing required parameters')

    # Return the extracted parameters
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


def create_zip(images):
    """
    Create a ZIP file containing the given images.

    Args:
        images (list): A list of paths to image files.

    Returns:
        str or None: The name of the created ZIP file if successful, None otherwise.
    """
    if all(os.path.exists(image_path) for image_path in images):
        with ZipFile('../images.zip', 'w') as zip_file:
            for image_path in images:
                zip_file.write(image_path, os.path.basename(image_path))
        return 'images.zip'
    else:
        return None



# def your_route_function():
#     """
#     Your Flask route function to handle the request.
#
#     Returns:
#         str or Response: A response indicating success or failure.
#     """
#     zip_file = create_zip(image_paths)
#     if zip_file:
#         return send_file(zip_file, mimetype='application/zip', as_attachment=True)
#     else:
#         return 'One or more images not found', 404
