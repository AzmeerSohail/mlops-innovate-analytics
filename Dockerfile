# Use an official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip


# Command to run your app (e.g., a training script or Flask app)
CMD ["python", "ml_code/example.py"]
