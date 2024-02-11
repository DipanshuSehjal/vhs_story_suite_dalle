# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

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


if __name__ == '__main__':
    app.run(debug=True)
