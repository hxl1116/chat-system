from src.db.utils import commit, fetch_many, fetch_one


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


def insert_member(last, first, user, email, user_change_date):
    commit("""
        INSERT INTO member VALUES (last_name=%s, first_name=%s, username=%s, email=%s, username_changed_date=%s)
    """, (last, first, user, email, user_change_date))


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
