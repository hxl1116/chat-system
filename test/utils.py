import requests

from src.api.utils import ResCode
from src.db.utils import connect, reload_data


def reload_test_data():
    reload_data()


def assert_sql_count(test, sql, params=None, n=0, msg='Expected row count did not match query'):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, params) if params else cur.execute(sql)
    test.assertEqual(n, cur.rowcount, msg)
    conn.close()


def get_rest_call(test, url, params=None, expected_code=ResCode.SUCCESS.value):
    response = requests.get(url, params)
    test.assertEqual(expected_code, response.status_code, f'Response code to {url} not {expected_code}')

    return response.json()


def put_rest_call(test, url, data=None, expected_code=ResCode.CREATED.value):
    response = requests.put(url, data)
    test.assertEqual(expected_code, response.status_code, f'Response code to {url} not {expected_code}')

    return response.json()


def post_rest_call(test, url, data=None, expected_code=ResCode.CREATED.value):
    response = requests.post(url, data)
    test.assertEqual(expected_code, response.status_code, f'Response code to {url} not {expected_code}')

    return response.json()


def del_rest_call(test, url, expected_code=ResCode.NO_CONTENT.value):
    response = requests.delete(url)
    test.assertEqual(expected_code, response.status_code, f'Response code to {url} not {expected_code}')
