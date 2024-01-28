# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Flask application code into the container
COPY app.py .

# Expose the port that your Flask application will listen on
EXPOSE 5000

# Define the command to run your Flask application
CMD ["python", "app.py"]
