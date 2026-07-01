import sqlite3
import os

DB_Path = os.path.join("Data", "documents.db")

def get_connection():
    return sqlite3.connect(DB_Path)

def init_DB():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        path TEXT,
        thumbnail_path TEXT,
        tags TEXT,
        description TEXT,
        upload_date TEXT,
        lecture_date TEXT,
        total_pages INTEGER
        )
    """
    )
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS page_visits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        document_id INTEGER,
        page_number INTEGER,
        timestamp TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS app_visits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_type TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    print("DB operation successfull.")
    conn.close()