import os

def get_config():
    return {
        "DB_FILE": os.getenv("DB_FILE", "events.db"),
        "OLLAMA_MODEL": os.getenv("OLLAMA_MODEL", "mistral"),
        "GMAIL_SCOPES": ['https://www.googleapis.com/auth/gmail.readonly']
    }

conf = get_config()