from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import psycopg2
from psycopg2 import OperationalError
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)


# Database connection setup
DB_HOST = "db"
DB_NAME = "sec_db"
DB_USER = "admin"
DB_PASSWORD = "a1a1a1"


# Basic home route
@app.route('/')
def home():
    return "Welcome to the add_friend API!"  # or render a homepage or documentation page


@app.route('/add_friend', methods=['POST'])
def add_friend():
    try:
        # Extract data from the JSON body
        data = request.json  # This will get the JSON sent in the body
        phone_number = data.get('phone_number')
        name = data.get('name')
        surname = data.get('surname')
        address = data.get('address')
        birthday = data.get('birthday')
        remark = data.get('remark')

        if not phone_number:
            raise ValueError("Phone number is required")

        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()

        # Insert the friend data into the database
        cursor.execute("""
            INSERT INTO friends (phone_number, name, surname, address, birthday, remark, date_created)
            VALUES (%s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP)
            RETURNING phone_number
        """, (phone_number, name, surname, address, birthday, remark))

        conn.commit()
        cursor.close()
        conn.close()

        # Return success response
        return jsonify({
            'status': 'success',
            'message': 'Friend added successfully'
        }), 200

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
    app.run(host='0.0.0.0', port=5005, debug=True)
