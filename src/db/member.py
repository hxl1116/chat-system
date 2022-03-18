from psycopg2.sql import Identifier, SQL

from .utils import commit, fetch_many, fetch_one


def member_exists(id=None, email=None):
    if id:
        return True if fetch_one("""
                        SELECT 1 FROM member WHERE member_id = %s
                    """, (id,)) else False
    if email:
        return True if fetch_one("""
                                SELECT 1 FROM member WHERE email = %s
                            """, (email,)) else False


def get_member_hashword(email):
    return fetch_one("""
        SELECT password FROM member WHERE email = %s
    """, (email,))


# TODO: Test
def fetch_member(id):
    return fetch_one("""
        SELECT * FROM member WHERE member_id = %s
    """, (id,))


# TODO: Test
def fetch_all_members():
    return fetch_many("""
        SELECT * FROM member
    """)


# TODO: Test
def insert_member(last, first, user, email):
    commit("""
        INSERT INTO member (last_name, first_name, username, email) VALUES (%s, %s, %s, %s)
    """, (last, first, user, email))


def update_member(id, **kwargs):
    query = SQL("UPDATE member SET ({}) = %s WHERE member_id = %s").format(
        SQL(', ').join(map(Identifier, list(kwargs.keys())))
    )

    commit(query, (tuple(kwargs.values()), id))


# TODO: Test
def delete_member(id):
    commit("""
        DELETE FROM member WHERE member_id = %s
    """, (id,))
