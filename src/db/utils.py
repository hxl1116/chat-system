import os

import psycopg2
import yaml


def connect():
    yml_path = os.path.join(os.path.dirname(__file__), '../../config/db.yml')

    with open(yml_path, 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    return psycopg2.connect(dbname=config['database'],
                            user=config['user'],
                            password=config['password'],
                            host=config['host'],
                            port=config['port'])


def exec_sql_file(path):
    full_path = os.path.join(os.path.dirname(__file__), path)

    conn = connect()
    cur = conn.cursor()

    with open(full_path, 'r') as file:
        cur.execute(file.read())

    conn.commit()
    conn.close()


def fetch_one(sql, args=None):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    one = cur.fetchone()
    conn.close()

    return one


def fetch_many(sql, args=None):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    list_of_tuples = cur.fetchall()
    conn.close()

    return list_of_tuples


def commit(sql, args=None):
    conn = connect()
    cur = conn.cursor()
    query = cur.mogrify(sql, args)
    result = cur.execute(query)
    conn.commit()
    conn.close()

    return result


def rebuild_tables():
    exec_sql_file('../../res/schema.sql')


def reload_routines():
    exec_sql_file('../../res/routines/functions.sql')
    exec_sql_file('../../res/routines/procedures.sql')
    exec_sql_file('../../res/routines/triggers.sql')


def reload_data():
    commit("CALL reload_test_data()")


def init_db():
    reload_routines()
    rebuild_tables()
    reload_data()
