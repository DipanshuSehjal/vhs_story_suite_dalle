# app.py
from flask import Flask, request, jsonify, send_file
import os
from zipfile import ZipFile
from flask_cors import CORS
import io
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes


@app.route('/api/data', methods=['POST'])
def receive_data():
    # Dummy data to simulate storing stories
    stored_stories = []
    data = request.json
    title = data.get('title')
    description = data.get('description')
    genre = data.get('genre')
    print("call executed")
    # Process the received data (e.g., save to database or list)
    stored_stories.append({'title': title, 'description': description, 'genre': genre})

    # Return a response with the received story details and a success message
    response_data = {
        'message': 'Story submitted successfully',
        'story': {'title': title, 'description': description, 'genre': genre}
    }
    return jsonify(response_data)


@app.route('/')
def hello():
    # Your logic to fetch or compute data
    return jsonify({'message': 'Hello from Flask!'})


@app.route('/api/data')
def get_data():
    # Your logic to fetch or compute data
    return jsonify({'message': 'Running your app'})


@app.route('/submit', methods=['POST'])
def submit():
    if not request.is_json:
        # Request does not contain JSON data
        # Handle the case when the request is not JSON
        return jsonify({'error': 'Request must contain JSON data'}), 400

    # Parse JSON data from the request body
    request_data = request.json

    # Get input text from the JSON data
    input_text = request_data.get('text')
    print(input_text)

    # if not input_text:
    #     return "Invalid prompt", 404

    image_paths = [
        'images/a_painting_of_man_waiting_for_hi.png',
        'images/a_painting_of_man_waiting_for_hi_1.png',
        'images/a_painting_of_man_waiting_for_hi_2.png',
        'images/a_painting_of_man_waiting_for_hi_3.png',
        'images/a_painting_of_man_waiting_for_hi_4.png',
        'images/a_painting_of_man_waiting_for_hi_5.png',
    ]

    # Check if all images exist
    if all(os.path.exists(image_path) for image_path in image_paths):
        # Create a temporary ZIP file
        with ZipFile('images.zip', 'w') as zip_file:
            # Add each image to the ZIP file
            for image_path in image_paths:
                zip_file.write(image_path, os.path.basename(image_path))

        # Return the ZIP file as a response
        return send_file('images.zip', mimetype='application/zip',
                         as_attachment=True)
    else:
        return 'One or more images not found', 404


def generate_image(text):
    # Create a blank image
    img = Image.new('RGB', (300, 100), color='white')

    # Initialize ImageDraw object
    draw = ImageDraw.Draw(img)

    # Choose a font and size
    font = ImageFont.load_default()

    # Calculate text size and position
    text_width, text_height = draw.textsize(text, font=font)
    position = ((img.width - text_width) // 2, (img.height - text_height) // 2)

    # Draw text on the image
    draw.text(position, text, fill='black', font=font)

    return img


if __name__ == '__main__':
    app.run(debug=True)
