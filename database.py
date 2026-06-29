import sqlite3
from config import DATABASE

conn = sqlite3.connect(DATABASE, check_same_thread=False)
cursor = conn.cursor()


def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY,
        first_name TEXT,
        username TEXT,
        joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        banned INTEGER DEFAULT 0
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS downloads(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        file_name TEXT,
        file_size INTEGER,
        status TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS settings(
        key TEXT PRIMARY KEY,
        value TEXT
    )
    """)

    conn.commit()


def add_user(user):
    cursor.execute(
        """
        INSERT OR IGNORE INTO users(user_id, first_name, username)
        VALUES(?,?,?)
        """,
        (
            user.id,
            user.first_name,
            user.username
        )
    )
    conn.commit()


def is_banned(user_id):
    cursor.execute(
        "SELECT banned FROM users WHERE user_id=?",
        (user_id,)
    )
    row = cursor.fetchone()

    if row is None:
        return False

    return row[0] == 1


def ban_user(user_id):
    cursor.execute(
        "UPDATE users SET banned=1 WHERE user_id=?",
        (user_id,)
    )
    conn.commit()


def unban_user(user_id):
    cursor.execute(
        "UPDATE users SET banned=0 WHERE user_id=?",
        (user_id,)
    )
    conn.commit()


def total_users():
    cursor.execute(
        "SELECT COUNT(*) FROM users"
    )
    return cursor.fetchone()[0]


def add_download(user_id, filename, filesize, status):
    cursor.execute(
        """
        INSERT INTO downloads
        (user_id,file_name,file_size,status)
        VALUES(?,?,?,?)
        """,
        (
            user_id,
            filename,
            filesize,
            status
        )
    )

    conn.commit()


create_tables()
