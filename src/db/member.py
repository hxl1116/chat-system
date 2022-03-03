from db.utils import fetch_many


def fetch_all_members():
    return fetch_many("""
        SELECT *
        FROM member
    """)
