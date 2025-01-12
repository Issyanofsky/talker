from flask import Flask, request, jsonify
import os
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)

# This ensures /add_friend and /add_friend/ are treated as the same route
app.url_map.strict_slashes = False

CORS(app)  # This enables CORS for all routes

# Folder where the files will be saved
SAVE_FOLDER = '/app/listner'
# os.makedirs(SAVE_FOLDER, exist_ok=True)


# Basic home route
@app.route('/')
def home():
    return "Welcome to the file_save API!"  # or render a homepage or documentation page


@app.route('/save_text', methods=['POST'])
def save_text():
    # Get the phone number and text from the request
    data = request.get_json()

    phone_number = data.get('phone_number')
    text = data.get('text')

    if not phone_number or not text:
        return jsonify({'error': 'Phone number and text are required'}), 400

    # Create the file name using the phone number + timestamp
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = f"{phone_number}_{timestamp}.txt"
    file_path = os.path.join(SAVE_FOLDER, file_name)

    # Save the text to the file
    with open(file_path, 'w') as file:
        file.write(text)

    # Return the file name as response
    return jsonify({'file_name': file_name}), 200


@app.route('/get_file/<file_name>', methods=['GET'])
def get_file(file_name):
    # Get the full file path
    file_path = os.path.join(SAVE_FOLDER, file_name)

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        return jsonify({'file_name': file_name, 'content': content}), 200
    else:
        return jsonify({'error': 'File not found'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, debug=True)
