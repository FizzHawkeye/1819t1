# Use the official ubuntu base image
FROM python:3.6

# Set working directory to /app
WORKDIR /app

# Copy our application file into the image
COPY app.py /app

# Install our dependency (Flask in this case)
RUN pip install Flask

# Run app.py when the container is launched
EXPOSE 5000
CMD ["python", "app.py"]
