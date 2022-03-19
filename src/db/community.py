from db.utils import fetch_many, fetch_one


def community_exists(id):
    return True if fetch_one("""
            SELECT 1 FROM community WHERE community_id = %s
        """, (id,)) else False


def fetch_all_communities():
    return fetch_many("""
        SELECT *
        FROM community
    """)
