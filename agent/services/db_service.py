import sqlite3

from config.config import conf

class DatabaseService:
    def __init__(self):
        self.db_file = conf["DB_FILE"]
        self._init_db()

    def _connect(self):
        return sqlite3.connect(self.db_file)

    def _init_db(self):
        with self._connect() as conn:
            c = conn.cursor()
            c.execute('''
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    event_start TEXT,
                    event_end TEXT,
                    location TEXT,
                    email_id TEXT UNIQUE,
                    subject TEXT,
                    body TEXT
                )
            ''')
            conn.commit()

    def save_event(self, event, email_id, subject, body):
        with self._connect() as conn:
            c = conn.cursor()
            c.execute('''
                INSERT OR IGNORE INTO events 
                (name, event_start, event_end, location, email_id, subject, body)
                VALUES (?, ?, ?, ?, ?, ?, ?)''',
                      (
                          event.get('event_name', 'Unknown'),
                          event.get('event_start', 'Unknown'),
                          event.get('event_end', 'Unknown'),
                          event.get('event_location', 'Unknown'),
                          email_id,
                          subject,
                          body
                      ))
            conn.commit()

    def get_events(self, limit):
        with self._connect() as conn:
            c = conn.cursor()
            c.execute(f"SELECT id, name, event_start, event_end, location FROM events ORDER BY id LIMIT {limit}")
            return c.fetchall()

    def get_event_by_name(self, name):
        with self._connect() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM events WHERE name LIKE ?", (f"%{name}%",))
            return c.fetchone()

    def is_email_already_saved(self, email_id):
        with self._connect() as conn:
            c = conn.cursor()
            c.execute("SELECT 1 FROM events WHERE email_id = ?", (email_id,))
            return c.fetchone() is not None

db_client = DatabaseService()