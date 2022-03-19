import unittest
from unittest import TestCase

import requests

from src.db.member import fetch_all_members
from test.utils import reload_test_data, assert_sql_count, get_rest_call, put_rest_call, post_rest_call, del_rest_call

SIGNUP_ENDPOINT = 'http://127.0.0.1:5000/signup'
LOGIN_ENDPOINT = 'http://127.0.0.1:5000/login'
MEMBERS_ENDPOINT = 'http://127.0.0.1:5000/members'


class TestMember(TestCase):
    TEST_MEMBER = {
        'user': 'lab-rat',
        'pass': 'Str0ngP@ssword22',
        'first': 'Johnny',
        'last': 'Test',
        'email': 'johnny@test.com'
    }

    def setUp(self) -> None:
        reload_test_data()

        # Create test member
        requests.post(SIGNUP_ENDPOINT, data=self.TEST_MEMBER)

        # Login as test member
        res = requests.post(LOGIN_ENDPOINT, data={'user': self.TEST_MEMBER['user'], 'pass': self.TEST_MEMBER['pass']})

        self.session_key = res.json()['session_key']

        self.members = fetch_all_members()
        self.params = {
            'last': 'Larson',
            'first': 'Henry',
            'user': 'neutron_chicken',
            'email': 'hxl1116@g.rit.edu'
        }

    def test_get(self):
        res = get_rest_call(test=self, url=MEMBERS_ENDPOINT, params={'member': self.TEST_MEMBER['user']},
                            headers={'Session-Key': self.session_key})
        assert_sql_count(self, sql="SELECT * FROM member", n=len(res))

    @unittest.skip('POST for Member does not exist')
    def test_post(self):
        post_rest_call(self, MEMBERS_ENDPOINT, data=self.params, headers={'Session-Key': self.session_key})

        assert_sql_count(self, sql="SELECT * FROM member", n=len(self.members) + 1)

    def test_put(self):
        member = self.members[0]
        put_rest_call(test=self, url=f'{MEMBERS_ENDPOINT}/{member["member_id"]}', data=self.params,
                      headers={'Session-Key': self.session_key})
        assert_sql_count(self, sql="SELECT * FROM member", n=len(self.members))

    def test_delete(self):
        member = self.members[0]
        del_rest_call(test=self, url=f'{MEMBERS_ENDPOINT}/{member["member_id"]}', headers={'Session-Key': self.session_key})
        assert_sql_count(self, sql="SELECT * FROM member", n=len(self.members) - 1)

    @classmethod
    def tearDownClass(cls) -> None:
        reload_test_data()
