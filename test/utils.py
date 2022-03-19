import requests

from src.api.utils import ResCode
from src.db.utils import connect, reload_data

TEST_MEMBER = {
    'user': 'lab-rat',
    'pass': 'Str0ngP@ssword22',
    'first': 'Johnny',
    'last': 'Test',
    'email': 'johnny@test.com'
}

BAD_ID = '00000000-0000-0000-0000-000000000000'

SIGNUP_ENDPOINT = 'http://127.0.0.1:5000/signup'
LOGIN_ENDPOINT = 'http://127.0.0.1:5000/login'
CHANNELS_ENDPOINT = 'http://127.0.0.1:5000/channels'
COMMUNITIES_ENDPOINT = 'http://127.0.0.1:5000/communities'
DIRECT_MSGS_ENDPOINT = 'http://127.0.0.1:5000/dms'
MEMBERS_ENDPOINT = 'http://127.0.0.1:5000/members'


def reload_test_data():
    reload_data()


def signup_test_member():
    # Create test member
    requests.post(SIGNUP_ENDPOINT, data=TEST_MEMBER)


def login_test_member():
    # Login as test member
    return requests.post(LOGIN_ENDPOINT, data={'user': TEST_MEMBER['user'], 'pass': TEST_MEMBER['pass']})


def assert_sql_count(test, sql, params=None, n=0, msg='Expected row count did not match query'):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, params) if params else cur.execute(sql)
    test.assertEqual(n, cur.rowcount, msg)
    conn.close()


def get_rest_call(test, url, params=None, headers=None, expected_code=ResCode.SUCCESS.value):
    response = requests.get(url, params, headers=headers)
    test.assertEqual(expected_code, response.status_code, f'Response code to {url} not {expected_code}')

    return response.json()


def put_rest_call(test, url, data=None, headers=None, expected_code=ResCode.CREATED.value):
    response = requests.put(url, data, headers=headers)
    test.assertEqual(expected_code, response.status_code, f'Response code to {url} not {expected_code}')

    return response.json()


def post_rest_call(test, url, data=None, headers=None, expected_code=ResCode.CREATED.value):
    response = requests.post(url, data, headers=headers)
    test.assertEqual(expected_code, response.status_code, f'Response code to {url} not {expected_code}')

    return response.json()


def del_rest_call(test, url, headers=None, expected_code=ResCode.NO_CONTENT.value):
    response = requests.delete(url, headers=headers)
    test.assertEqual(expected_code, response.status_code, f'Response code to {url} not {expected_code}')
