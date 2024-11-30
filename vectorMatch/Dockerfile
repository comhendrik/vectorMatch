# Use the official Python image as the base image
FROM python:3.11-slim


# Set the working directory inside the container
WORKDIR /app

# Copy the entire current directory (including subdirectories) to /app in the container
COPY . /app

# Install the required Python packages from requirements.txt (if available)
# If you don't have a requirements.txt file, you can skip this step or add necessary packages manually.
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the application will run on (adjust as needed)
EXPOSE 8000

# Command to run the Python application
# You can replace 'app.py' with the entry point of your application
CMD ["python", "main.py"]
