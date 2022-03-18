# from src.db.models.channel import Channel

from src.db.utils import fetch_many


def fetch_all_channels():
    return fetch_many("""
        SELECT * FROM channel
    """)

# def fetch_all_channels():
#     return Channel.query.all()
