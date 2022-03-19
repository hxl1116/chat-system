import unittest
from unittest import TestCase

from test.utils import reload_test_data, signup_test_member, login_test_member, get_rest_call, post_rest_call, \
    assert_sql_count, TEST_MEMBER, DIRECT_MSGS_ENDPOINT


class TestDirect(TestCase):
    def setUp(self) -> None:
        reload_test_data()
        signup_test_member()
        res = login_test_member()

        self.session_key = res.json()['session_key']

    def test_get(self):
        res = get_rest_call(test=self, url=f'{DIRECT_MSGS_ENDPOINT}/spicelover',
                            headers={'Session-Key': self.session_key, 'member': TEST_MEMBER['user']})

        assert_sql_count(test=self, sql="SELECT * FROM direct_message", n=len(res))

    @unittest.skip('not implemented')
    def test_post(self):
        # post_rest_call()
        # assert_sql_count()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        reload_test_data()
