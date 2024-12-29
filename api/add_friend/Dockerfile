# Use a base image with Python
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY add_friend_api.py /app/add_friend_api.py

# Install the required dependencies
RUN pip install --upgrade pip && pip install Flask psycopg2-binary

RUN pip install flask-cors

# Expose the port the app will run on
EXPOSE 5005

# Command to run the Flask app
CMD ["python", "add_friend_api.py"]
