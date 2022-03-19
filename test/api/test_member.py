from unittest import TestCase

from db.member import fetch_all_members
from test.utils import TEST_MEMBER, MEMBERS_ENDPOINT, signup_test_member, login_test_member, reload_test_data, \
    assert_sql_count, get_rest_call, put_rest_call, del_rest_call


class TestMember(TestCase):
    def setUp(self) -> None:
        reload_test_data()
        signup_test_member()
        res = login_test_member()

        self.session_key = res.json()['session_key']

        self.members = fetch_all_members()
        self.params = {
            'last': 'Larson',
            'first': 'Henry',
            'user': 'neutron_chicken',
            'email': 'hxl1116@g.rit.edu'
        }

    def test_get(self):
        res = get_rest_call(test=self, url=MEMBERS_ENDPOINT, params={'member': TEST_MEMBER['user']},
                            headers={'Session-Key': self.session_key, 'member': TEST_MEMBER['user']})
        assert_sql_count(self, sql="SELECT * FROM member", n=len(res))

    def test_put(self):
        member = self.members[0]
        put_rest_call(test=self, url=f'{MEMBERS_ENDPOINT}/{member["member_id"]}', data=self.params,
                      headers={'Session-Key': self.session_key, 'member': TEST_MEMBER['user']})
        assert_sql_count(self, sql="SELECT * FROM member", n=len(self.members))

    def test_delete(self):
        member = self.members[0]
        del_rest_call(test=self, url=f'{MEMBERS_ENDPOINT}/{member["member_id"]}',
                      headers={'Session-Key': self.session_key, 'member': TEST_MEMBER['user']})
        assert_sql_count(self, sql="SELECT * FROM member", n=len(self.members) - 1)

    @classmethod
    def tearDownClass(cls) -> None:
        reload_test_data()
