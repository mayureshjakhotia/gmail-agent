import json

from utils.email_utils import clean_email_body
from utils.config import conf


class OllamaService:
    def __init__(self, model_name):
        from ollama import Client
        self.model_name = model_name
        self.client = Client()

    def extract_event_info(self, subject, raw_body, max_body_chars=2000):
        # Clean and truncate body
        body = clean_email_body(raw_body)
        if len(body) > max_body_chars:
            body = body[:max_body_chars]

        prompt = f"""
    You are a smart email parser.

    Extract the following fields from the email and return them as a valid JSON object:

    - event_name → If the email mentions who invited or is hosting, combine their name with the event name, e.g., "Jack Robbins - Busy in workshop"
    - event_start → Full date and time: YYYY-MM-DD HH:MM AM/PM (skip time if not provided)
    - event_end → Full date and time: YYYY-MM-DD HH:MM AM/PM (skip time if not provided)
    - event_location → Physical (e.g. California, Mumbai) or virtual (e.g., "Google Meet", "Zoom", etc.)

    Rules:
    - If no host name is explicitly mentioned, just return the event name.
    - Do not assume the name from the email sender or account name.
    - ONLY use what is in the email body or subject.
    - If any value is missing, return "Unknown".
    - Respond ONLY in JSON.

    --- Subject ---
    {subject}

    --- Body ---
    {body}
    """

        try:
            response = self.client.chat(
                model=conf["OLLAMA_MODEL"],
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            output = response['message']['content']
            print(f"Raw model output: {output}")
            return json.loads(output)
        except json.JSONDecodeError:
            print(f"JSON parsing failed. Raw output: {output}")
            return {}
        except Exception as e:
            print(f"Ollama error: {e}")
            return {}

ollama_client = OllamaService(model_name="mistral")
