# Use the official Python image
FROM python:3.8

# Copy the current directory contents into the container
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Install Flask and other required dependencies
RUN pip install Flask
RUN pip install psycopg2

# Expose port 5000 for the Flask development server
EXPOSE 5000

#Setup environment variables
ENV FLASK_APP=watchlist_api_postgres.py

# Run the Flask development server when the container starts
CMD ["flask", "run"]
