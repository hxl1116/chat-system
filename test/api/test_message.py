from unittest import TestCase

from src.db.member import fetch_member
from src.db.messages.direct import fetch_many_dms
from test.utils import reload_test_data, signup_test_member, login_test_member, get_rest_call, post_rest_call, \
    assert_sql_count, TEST_MEMBER, DM_LIMIT, DIRECT_MSGS_ENDPOINT


class TestDirect(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        reload_test_data()

        cls.dm_count = len(fetch_many_dms(user='spicelover', limit=None))

    def setUp(self) -> None:
        reload_test_data()
        signup_test_member()
        res = login_test_member()

        self.session_key = res.json()['session_key']

        self.spicelover_id = fetch_member(user='spicelover')['member_id']
        self.sihaya_id = fetch_member(user='sihaya')['member_id']

    def test_get(self):
        res = get_rest_call(test=self, url=f'{DIRECT_MSGS_ENDPOINT}/spicelover',
                            headers={'Session-Key': self.session_key, 'member': TEST_MEMBER['user']})

        assert_sql_count(test=self, sql="SELECT * FROM direct_message", n=len(res))

    def test_get_with_limit(self):
        get_rest_call(test=self, url=f'{DIRECT_MSGS_ENDPOINT}/spicelover', params={'Limit': DM_LIMIT},
                      headers={'Session-Key': self.session_key, 'member': TEST_MEMBER['user']})

        assert_sql_count(test=self, sql="SELECT * FROM direct_message LIMIT %s", params=(DM_LIMIT,), n=DM_LIMIT)

    def test_post(self):
        post_rest_call(test=self, url=DIRECT_MSGS_ENDPOINT,
                       data={'sender': self.spicelover_id, 'receiver': self.sihaya_id,
                             'content': 'Mind is the fear killer.'},
                       headers={'Session-Key': self.session_key, 'member': TEST_MEMBER['user']})

        assert_sql_count(test=self, sql="SELECT * FROM direct_message", n=self.dm_count + 1)

    @classmethod
    def tearDownClass(cls) -> None:
        reload_test_data()
