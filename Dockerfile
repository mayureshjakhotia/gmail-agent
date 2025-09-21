FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV OLLAMA_HOST=host.docker.internal
ENV PYTHONPATH=/app

# Expose any necessary ports (if applicable)
# EXPOSE 8000

# Change working directory to ensure correct module imports
WORKDIR /app/agent

# Keep the container running
CMD ["tail", "-f", "/dev/null"]
