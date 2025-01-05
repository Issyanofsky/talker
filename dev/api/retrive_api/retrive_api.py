from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

# Database connection settings
DB_SETTINGS = {
    "host": "db",  # 'db' is the service name from Docker Compose
    "dbname": "sec_db",
    "user": "admin",
    "password": "a1a1a1"
}

# Basic home route
@app.route('/')
def home():
    return "Welcome to the Retrive API!"  # or render a homepage or documentation page

# Route to handle requests with path parameters
@app.route('/friend/<phone_number>', methods=['GET'])
def get_friend(phone_number):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**DB_SETTINGS)
        cursor = conn.cursor()

        # Query the database for the friend's data
        query_friend = "SELECT * FROM friends WHERE phone_number = %s"
        cursor.execute(query_friend, (phone_number,))
        friend_result = cursor.fetchone()

        # If friend not found, return error
        if not friend_result:
            return jsonify({"error": "Friend not found"}), 404

        # Query the database for events related to the friend
        query_events = "SELECT * FROM events WHERE friend_phone_number = %s"
        cursor.execute(query_events, (phone_number,))
        events_result = cursor.fetchall()

        # Query the database for children related to the friend
        query_children = "SELECT * FROM children WHERE friend_phone_number = %s"
        cursor.execute(query_children, (phone_number,))
        children_result = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        # Constructing the response
        friend_data = {
            "phone_number": friend_result[0],
            "name": friend_result[1],
            "surname": friend_result[2],
            "address": friend_result[3],
            "birthday": friend_result[4],
            "remarks": friend_result[5]
        }

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

        children_data = []
        for child in children_result:
            children_data.append({
                "date": child[2],
                "description": child[3],
                "amount": child[4],
                "remarks": child[5]
            })

        # Return the data in the response
        return jsonify({
            "friend": friend_data,
            "events": events_data,
            "children": children_data
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
