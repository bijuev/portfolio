# Use the official Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port Gunicorn will run on
EXPOSE 8000

# Collect static files
RUN python manage.py collectstatic --noinput

# Command to run Gunicorn
CMD gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000
