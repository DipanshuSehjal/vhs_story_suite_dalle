from flask import Flask, request, jsonify
from flask_cors import CORS

from stability_ai.text_to_image import ImageGenerationConfig, TextToImageGenerator

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes


# Summary:
# The provided Flask app defines routes that accepts POST requests containing JSON data. The
# JSON data should include parameters related to image processing. The app extracts the required parameters from the
# JSON payload, performs necessary checks to ensure data integrity, and processes the parameters. It then returns the
# processed data as a JSON response. The code includes error handling to catch and handle exceptions gracefully.
# Overall, the app provides a modular and reliable backend for processing image-related tasks received from a
# front-end application.

@app.route('/api/text-to-image', methods=['POST'])
def text_to_image_handler():
    try:
        data = request.json  # Get JSON data from the request

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
        # text_prompts = data.get('text_prompts')
        positive_prompt = data.get('positivePrompt')
        negative_prompt = data.get('negativePrompt')

        ###### custom params ######
        # want 6 images or just 1 image output?
        multiple = data.get('multiple')
        # random types
        random = data.get('random')

        # Print the extracted parameters
        print("steps:", steps)
        print("width:", width)
        print("height:", height)
        print("seed:", seed)
        print("cfg_scale:", cfg_scale)
        print("samples:", samples)
        # print("text_prompts:", text_prompts)
        print("positive_prompt:", positive_prompt)
        print("negative_prompt:", negative_prompt)
        print("multiple:", multiple)
        print("random:", random)

        # Check if required parameters are present
        if None in [steps, width, height, seed, cfg_scale, samples, positive_prompt, negative_prompt]:
            return jsonify({'error': 'Missing required parameters'}), 400

        # Create a Config instance with the extracted parameters
        config = ImageGenerationConfig(steps=steps, width=width, height=height, seed=seed, cfg_scale=cfg_scale,
                                       samples=samples, positive_prompt=positive_prompt,
                                       negative_prompt=negative_prompt)

        # Create a TextToImageGenerator instance with the config
        generator = TextToImageGenerator(config=config)

        # Call the generate_images method
        # image = generator.generate_images()

        # image is boolean for the time being
#        if not image:
#            raise Exception
        # Return the processed data as JSON response
        # This is base64 image

        return generator.dummy_get_images_zip(), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Internal Server Error


@app.route('/api/image-to-image', methods=['POST'])
def image_to_image_handler():
    pass
    # # Extract parameters from the JSON data
    # data = request.json
    # # Extract parameters from the JSON data
    # steps = data.get('steps')
    # width = data.get('width')
    # height = data.get('height')
    # seed = data.get('seed')
    # cfg_scale = data.get('cfg_scale')
    # samples = data.get('samples')
    # style_preset = data.get('style_preset')
    # text_prompts = data.get('text_prompts')
    #
    # # Call the function for image-to-image functionality
    # result = image_to_image_function(steps, width, height, seed, cfg_scale, samples, style_preset, text_prompts)
    #
    # # Return the response
    # return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
