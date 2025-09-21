from services.db_service import db_client
from services.gmail_service import gmail_client
from services.ollama_service import ollama_client
from utils.email_utils import contains_event_keywords
from utils.logger import logger


def run_event_agent(limit=5):
    emails = gmail_client.fetch_emails(query="event", max_results=limit)
    logger.info(f"Fetched {len(emails)} emails")
    for email in emails:
        email_id = email['id']
        subject, body = gmail_client.get_email_content(email_id)

        if db_client.is_email_already_saved(email_id):
            continue

        if not contains_event_keywords(subject, body):
            logger.debug(f"Skipping email {email_id}: no event keywords found.")
            continue

        event = ollama_client.extract_event_info(subject, body)

        if event and event.get("event_name") and event["event_name"] != "Unknown":
            db_client.save_event(event, email_id, subject, body)
            logger.info(f"Saved: {event['event_name']}")
        else:
            logger.warning(f"Skipped email {email_id} — no event info.")


def run(limit=5, mode="show"):
    if mode == "scan":
        run_event_agent(limit=limit)
    elif mode == "show":
        events = db_client.get_events(limit=limit)
        for e in events:
            logger.info(f"[{e[0]}] {e[1]} from {e[2]} to {e[3]} at {e[4]}")
    else:
        raise Exception(f"Invalid mode: {mode}")
