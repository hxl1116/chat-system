from unittest import TestCase

from test.utils import TEST_MEMBER, reload_test_data, get_rest_call, assert_sql_count, signup_test_member, \
    login_test_member, COMMUNITIES_ENDPOINT


class TestCommunity(TestCase):
    def setUp(self) -> None:
        reload_test_data()
        signup_test_member()
        res = login_test_member()

        self.session_key = res.json()['session_key']

    def test_get(self):
        res = get_rest_call(self, COMMUNITIES_ENDPOINT,
                            headers={'Session-Key': self.session_key, 'member': TEST_MEMBER['user']})
        assert_sql_count(self, sql="SELECT * FROM community", n=len(res))

    @classmethod
    def tearDownClass(cls) -> None:
        reload_test_data()
