from db.utils import fetch_many


def fetch_all_messages(chan_id):
    return fetch_many("""
        SELECT *
        FROM message
        WHERE channel_id = %s
    """, (chan_id,))
