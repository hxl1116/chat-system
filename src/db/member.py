from .utils import commit, fetch_many, fetch_one


def member_exists(id):
    return True if fetch_one("""
                SELECT 1 FROM member WHERE member_id = %s
            """, (id,)) else False


def fetch_member(id):
    return fetch_one("""
        SELECT * FROM member WHERE member_id = %s
    """, (id,))


def fetch_all_members():
    return fetch_many("""
        SELECT * FROM member
    """)


def insert_member(last, first, user, email):
    commit("""
        INSERT INTO member (last_name, first_name, username, email) VALUES (%s, %s, %s, %s)
    """, (last, first, user, email))


# TODO: Test, generate dynamic query from **kwargs
def update_member(id, **kwargs):
    commit("""
        UPDATE member SET %s = %s WHERE member_id=%s
    """, )


# TODO: Test
def delete_member(id):
    commit("""
        DELETE FROM member WHERE member_id = %s
    """, (id,))
