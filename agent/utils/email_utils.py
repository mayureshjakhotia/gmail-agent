import re
import html

def contains_event_keywords(subject, body):
    keywords = [
        "event", "ticket", "tickets", "waitlist", "register",
        "rsvp", "join us", "schedule", "conference", "webinar", "meetup",
        "festival", "show", "exhibition", "opening", "launch", "celebration",
        "party", "ceremony"
    ]
    combined_text = (subject + " " + body).lower()
    return any(keyword in combined_text for keyword in keywords)


def clean_email_body(body: str) -> str:
    # Decode HTML entities like &#847;
    body = html.unescape(body)

    # Normalize newlines
    body = body.replace('\r\n', '\n').replace('\r', '\n')

    # Remove invisible and non-printable Unicode characters
    invisible_chars_pattern = (
        r'[\u00ad\u034f\u200b\u200c\u200d\u2060\u00a0\u180e\u2028\u2029\u202f\u205f\u3000\u2007\u2008\u2009\u2003]'
    )
    body = re.sub(invisible_chars_pattern, '', body)

    # Remove numeric HTML entities like &#847; or &#8199;
    body = re.sub(r'&#\d+;', '', body)

    # Remove URLs
    body = re.sub(r'https?://\S+', '', body)

    # Remove boilerplate phrases
    boilerplate_phrases = [
        r'contact us',
        r'privacy policy',
        r'terms of service',
        r'unsubscribe',
        r'view in browser',
        r'update preferences',
        r'©\s*\d{4}',
        r'all rights reserved',
        r'\[.*?\]'
    ]
    for phrase in boilerplate_phrases:
        body = re.sub(phrase, '', body, flags=re.IGNORECASE | re.MULTILINE)

    # Remove multiple blank lines
    body = re.sub(r'\n\s*\n+', '\n\n', body)

    # Keep only lines with meaningful text
    lines = [line.strip() for line in body.split('\n') if len(line.strip()) > 3]
    body = '\n'.join(lines)

    return body.strip()
