from unittest import TestCase

from src.api.utils import ResCode
from db.member import fetch_all_members
from test.utils import reload_test_data, post_rest_call, assert_sql_count

SIGNUP_ENDPOINT = 'http://127.0.0.1:5000/signup'
LOGIN_ENDPOINT = 'http://127.0.0.1:5000/login'
LOGOUT_ENDPOINT = 'http://127.0.0.1:5000/logout'


class TestAuth(TestCase):
    def setUp(self) -> None:
        reload_test_data()

        self.params = {
            'last': 'Larson',
            'first': 'Henry',
            'user': 'chicken_wing',
            'pass': 'Str0ngP@ssword22',
            'email': 'hxl1116@g.rit.edu'
        }

    def test_signup(self):
        post_rest_call(test=self, url=SIGNUP_ENDPOINT, data=self.params)
        assert_sql_count(test=self, sql="SELECT * FROM member", n=len(fetch_all_members()))

    def test_login(self):
        # Create the member
        post_rest_call(test=self, url=SIGNUP_ENDPOINT, data=self.params)

        # Login with member
        post_rest_call(test=self, url=LOGIN_ENDPOINT, data={'user': self.params['user'], 'pass': self.params['pass']},
                       expected_code=ResCode.SUCCESS.value)

        assert_sql_count(test=self, sql="SELECT * FROM member", n=len(fetch_all_members()))

    # @unittest.skip('not implemented')
    def test_logout(self):
        # Create the member
        post_rest_call(test=self, url=SIGNUP_ENDPOINT, data=self.params)

        # Login the member
        res = post_rest_call(test=self,
                             url=LOGIN_ENDPOINT,
                             data={'user': self.params['user'], 'pass': self.params['pass']},
                             expected_code=ResCode.SUCCESS.value)

        # Log out the member
        post_rest_call(test=self,
                       url=LOGOUT_ENDPOINT,
                       data={'user': self.params['user'], 'Session-Key': res['session_key']},
                       expected_code=ResCode.SUCCESS.value)
        # post_rest_call(test=self,
        #                url=LOGOUT_ENDPOINT,
        #                data={'user': self.params['user']},
        #                headers={'Session-Key': res['session_key']},
        #                expected_code=ResCode.SUCCESS.value)

        assert_sql_count(test=self, sql="SELECT * FROM member", n=len(fetch_all_members()))

    @classmethod
    def tearDownClass(cls) -> None:
        reload_test_data()
