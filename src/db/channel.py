from db.utils import fetch_many


def fetch_all_channels():
    return fetch_many("""
        SELECT *
        FROM channel
    """)
