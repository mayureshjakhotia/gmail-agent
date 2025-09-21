from services.db_service import db_client
from services.gmail_service import gmail_client
from services.ollama_service import ollama_client
from utils.email_utils import contains_event_keywords


def run_event_agent(query="event", limit=5):
    emails = gmail_client.fetch_emails(query=query, max_results=limit)
    print(f"Fetched {len(emails)} emails")
    for email in emails:
        email_id = email['id']
        subject, body = gmail_client.get_email_content(email_id)

        if db_client.is_email_already_saved(email_id):
            continue

        if not contains_event_keywords(subject, body):
            print(f"Skipping email {email_id}: no event keywords found.")
            continue

        event = ollama_client.extract_event_info(subject, body)

        if event and event.get("event_name") and event["event_name"] != "Unknown":
            db_client.save_event(event, email_id, subject, body)
            print(f"✅ Saved: {event['event_name']}")
        else:
            print(f"⚠️ Skipped email {email_id} — no event info.")


def run(query="event", limit=5, mode="scan"):
    print("🔄 Running event agent...")

    if mode == "scan":
        run_event_agent(query=query, limit=limit)
    elif mode == "list":
        events = db_client.list_events()
        id = 1
        for e in events:
            print(f"[{id}] {e[1]} from {e[2]} to {e[3]} at {e[4]}")
            id += 1
    else:
        raise Exception("Invalid mode")


