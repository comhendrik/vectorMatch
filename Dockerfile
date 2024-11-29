# Use the Ollama base image
FROM ollama/ollama:latest

# Install required system packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Install the LLM Llama3.2 using Ollama
RUN ollama install llama3.2

# Set the working directory in the container
WORKDIR /app

# Copy the entire project directory into the container
COPY . /app

# Install Python dependencies (if requirements.txt exists)
RUN if [ -f "requirements.txt" ]; then pip3 install --no-cache-dir -r requirements.txt; fi

# Expose a port (if your Python app uses one)
EXPOSE 8000

# Set the default command to run the Python application
CMD ["python3", "app.py"]