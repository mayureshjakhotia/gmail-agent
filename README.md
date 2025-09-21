# Gmail Agent

## Security Warning

### Credentials File
The `credentials.json` file is a sensitive authentication file for Google OAuth. It contains:
- Private client credentials
- OAuth 2.0 configuration
- Confidential information specific to your Google Cloud project

**IMPORTANT SECURITY GUIDELINES:**
- NEVER commit this file to version control
- NEVER share this file publicly
- Keep it strictly confidential

### How to Obtain credentials.json
1. Go to the Google Cloud Console
2. Create a new project or select an existing one
3. Enable the Gmail API
4. Create OAuth 2.0 credentials
5. Download the credentials file
6. Place it in the project root directory

### .gitignore Protection
Ensure `credentials.json` is listed in your `.gitignore` file to prevent accidental commits.

## Setup and Installation

### Prerequisites

- Ollama
- Python 3.8+
- Docker
- Docker Compose

### Local Ollama Setup

Before running the Docker container, ensure Ollama is running locally:

```bash
# Start Ollama service
ollama serve

# Pull the Mistral model
ollama pull mistral
```

### 1. Clone the Repository

```bash
git clone https://github.com/mayureshjakhotia/gmail-agent.git
cd gmail-agent
```

### 2. Run the Application

```bash
# Build and start the Docker container
docker-compose up --build
```
### 3. Log into the container

```bash
docker exec -it gmail-agent-gmail-agent-1 /bin/bash
```

### 4. Stop the Application

```bash
docker-compose down
```

## Application Usage

Basic usage:
```bash
cd agent
python -m main  --mode <scan|show>  --limit <int>
```

## Configuration

- Ensure your configuration files are properly set up in the `agent/config/` directory before running.

## Troubleshooting

- Verify Ollama is running locally
- Check Docker container logs with `docker-compose logs`
- Ensure all configuration files are correctly mounted

## Dependencies

- Python 3.8+
- Docker
- Docker Compose
- Ollama
