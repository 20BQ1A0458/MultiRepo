# Use Python 3.8-slim as the base image
FROM python:3.8-slim

# Set working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the required Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code into the container
COPY . /app/

# Expose the port that Flask will run on
EXPOSE 5001

# Command to run the Flask application
CMD ["python", "app.py"]


