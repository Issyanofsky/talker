from flask import Flask, request, jsonify
import psycopg2
import requests
from flask_cors import CORS

app = Flask(__name__)

# This ensures /add_friend and /add_friend/ are treated as the same route
app.url_map.strict_slashes = False

CORS(app)  # This enables CORS for all routes

# Database connection setup
DB_HOST = "db"
DB_NAME = "sec_db"
DB_USER = "admin"
DB_PASSWORD = "a1a1a1"


# Basic home route
@app.route('/')
def home():
    return "Welcome to the add_event API!"  # or render a homepage or documentation page


# Route to add an event to the database
@app.route('/add_event', methods=['POST'])
def add_event():
    try:
        print("Request received")

        # Extract data from the request
        data = request.json  # This will get the JSON sent in the body
        print(f"Received data: {data}")

        phone_number = data.get('phone_number')
        event_date = data.get('event_date')
        summary = data.get('summary')

        # Check if the required fields are present
        if not phone_number or not event_date or not summary:
            raise ValueError("Missing required fields: phone_number, event_date, or summary")

        # Log the incoming data
        print(f"Received data: phone_number={phone_number}, event_date={event_date}, summary={summary}")

        # Step 1: Send a POST request to the first Flask API to get the file name
        file_save_api_url = "http://file-save-api/file_save"  # URL of your first Flask API
        response = requests.post(file_save_api_url, json={'phone_number': phone_number, 'text': summary})

        # Check if the first API request was successful
        if response.status_code != 200:
            return jsonify({'status': 'error', 'message': 'Error from file saving API'}), 500

        # Extract the file name from the response
        response_data = response.json()
        file_name = response_data.get('file_name')

        if not file_name:
            return jsonify({'status': 'error', 'message': 'No file_name returned from the first API'}), 500
        
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()

        # Insert the event data into the database
        cursor.execute("""
            INSERT INTO events (friend_phone_number, event_date, summary, keyword1, keyword2, keyword3, keyword4, keyword5, file_location)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING event_id
        """, (phone_number, event_date, summary, None, None, None, None, None, file_name))

        # Fetch the event ID of the newly inserted event
        event_id = cursor.fetchone()[0]

        # Query the database for the event data
        query_events = "SELECT * FROM events WHERE friend_phone_number = %s"
        cursor.execute(query_events, (phone_number,))
        events_result = cursor.fetchall()

        # Commit the transaction
        conn.commit()

        # Log the successful event ID
        print(f"Event added with event_id={event_id}")

        # Close the connection
        cursor.close()
        conn.close()

        # Prepare the event data for the response
        events_data = []
        for event in events_result:
            events_data.append({
                "event_date": event[2],
                "summary": event[3],
                "keyword1": event[4],
                "keyword2": event[5],
                "keyword3": event[6],
                "keyword4": event[7],
                "keyword5": event[8]
            })

        # Return success response
        return jsonify({
            'status': 'success',
            'message': 'Event added successfully',
            'event_id': event_id,  # Return the event_id of the newly added event
            'events': events_data  # Return all related events for the phone_number
        }), 200

    except psycopg2.Error as e:
        # Log specific PostgreSQL error
        print(f"PostgreSQL Error: {e}")
        return jsonify({'status': 'error', 'message': 'Database error: ' + str(e)}), 500

    except ValueError as e:
        # Log custom validation errors
        print(f"Validation Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 400

    except Exception as e:
        # Log any unexpected errors
        print(f"Unexpected Error: {e}")
        return jsonify({'status': 'error', 'message': 'Unexpected error: ' + str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
