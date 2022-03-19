from psycopg2.sql import Identifier, SQL

from db.utils import commit, fetch_many, fetch_one


def member_exists(id=None, user=None):
    if id:
        return True if fetch_one("""
                        SELECT 1 FROM member WHERE member_id = %s
                    """, (id,)) else False
    if user:
        return True if fetch_one("""
                                SELECT 1 FROM member WHERE username = %s
                            """, (user,)) else False


def get_member_hashword(user):
    return fetch_one("""
        SELECT password FROM member WHERE username = %s
    """, (user,))


def validate_session(user, session):
    return True if fetch_one("""
        SELECT 1 FROM member WHERE username = %s AND session_key = %s
    """, (user, session)) else False


def nullify_session(user):
    commit("""
        UPDATE member SET session_key = null, session_expire = null WHERE username = %s
    """, (user,))


def fetch_member(id):
    return fetch_one("""
        SELECT * FROM member WHERE member_id = %s
    """, (id,))


def fetch_all_members():
    return fetch_many("""
        SELECT * FROM member
    """)


def insert_member(**kwargs):
    commit("""
        INSERT INTO member (username, password, last_name, first_name, email) VALUES (%s, %s, %s, %s, %s)
    """, tuple(kwargs.values()))


def update_member(id, **kwargs):
    query = SQL("UPDATE member SET ({}) = %s WHERE member_id = %s").format(
        SQL(', ').join(map(Identifier, list(kwargs.keys()))))

    commit(query, (tuple(kwargs.values()), id))


def update_member_session(user, session_key, session_expire):
    commit("""
        UPDATE member SET (session_key, session_expire) = (%s, %s) WHERE username = %s
    """, (session_key, session_expire, user))


def delete_member(id):
    commit("""
        DELETE FROM member WHERE member_id = %s
    """, (id,))
