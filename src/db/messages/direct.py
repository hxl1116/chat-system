from ..utils import commit, fetch_many, fetch_one


def fetch_dm(id):
    return fetch_one("""
        SELECT * FROM direct_message WHERE message_id = %s
    """, (id,))


def fetch_many_dms(user, limit):
    return fetch_many("""
        SELECT message_id, sender_id, receiver_id, content, unread, timestamp
        FROM direct_message,
             member
        WHERE username = %s
          AND (sender_id = member_id OR receiver_id = member_id)
        LIMIT %s
    """, (user, limit)) if limit else fetch_many("""
        SELECT message_id, sender_id, receiver_id, content, unread, timestamp
        FROM direct_message,
             member
        WHERE username = %s
          AND (sender_id = member_id OR receiver_id = member_id)
    """, (user,))


def insert_dm(**kwargs):
    commit("""
        INSERT INTO direct_message (sender_id, receiver_id, content, timestamp) VALUES (%s, %s, %s, %s)
    """, (tuple(kwargs.values())))
