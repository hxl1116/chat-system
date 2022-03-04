from db.utils import fetch_many, commit


def fetch_all_members():
    return fetch_many("""
        SELECT *
        FROM member
    """)


# TODO: Add error handling
def insert_member(last, first, user, email, user_change_date):
    commit("""
        INSERT INTO member VALUES (last_name=%s, first_name=%s, username=%s, email=%s, username_changed_date=%s)
    """, (last, first, user, email, user_change_date))


# TODO: Generate dynamic query
def update_member(id, **kwargs):
    commit("""
        UPDATE member SET %s = %s WHERE member_id=%s
    """, )
