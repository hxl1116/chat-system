from src.db.utils import fetch_many


def fetch_all_communities():
    return fetch_many("""
        SELECT *
        FROM community
    """)
