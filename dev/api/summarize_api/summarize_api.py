from flask import Flask, request, jsonify
from flask_cors import CORS
from psycopg2 import OperationalError
import logging
import google.generativeai as genai
import os

# Setup logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# This ensures /add_friend and /summarize/ are treated as the same route
app.url_map.strict_slashes = False

# Enable CORS for all routes
CORS(app)


# Basic home route
@app.route('/')
def home():
    return "Welcome to the Summarize API!"  # or render a homepage or documentation page


@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        # Extract data from the JSON body
        data = request.json  # This will get the JSON sent in the body
        text = data.get('text')
        instruction = data.get('instruction')

        if not instruction or not text:
            raise ValueError("Missing Data to summarize")
        # connect to goole API
        genai.configure(api_key=os.getenv('GOOGLE_ACCESS_TOKEN'))

        model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction=instruction)
        response = model.generate_content(text)
        # Return the file name as response
        return response.text, 200

    except ValueError as e:
        logging.error(f"Value Error: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 400
    except OperationalError as e:
        logging.error(f"Database Error: {str(e)}")
        return jsonify({'status': 'error', 'message': 'Database error occurred'}), 500
    except Exception as e:
        logging.error(f"Unexpected Error: {str(e)}")
        return jsonify({'status': 'error', 'message': 'Failed to add friend'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007, debug=True)
