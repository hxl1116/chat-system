from .utils import fetch_many, fetch_one


def channel_exists(id):
    return True if fetch_one("""
        SELECT 1 FROM channel WHERE channel_id = %s
    """, (id,)) else False


def fetch_all_channels():
    return fetch_many("""
        SELECT * FROM channel
    """)
