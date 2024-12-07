# Use an official Python runtime as the base image
FROM python:3.12-slim

# Add metadata
LABEL authors="Mercy"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /movieapi

# Install system dependencies required for PostgreSQL and pip
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app will run on
EXPOSE 8000

# Command to start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
