# Use a base image with Python
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY retrive_api.py /app/retrive_api.py

# Copy the requirements.txt into the container
COPY requirements.txt /app/requirements.txt

# Install the required dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the port the app will run on
EXPOSE 5003

# Command to run the Flask app
CMD ["python", "retrive_api.py"]
