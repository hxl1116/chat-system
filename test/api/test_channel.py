from unittest import TestCase

from src.api.utils import ResCode
from src.db.channel import fetch_all_channels
from test.utils import TEST_MEMBER, signup_test_member, login_test_member, reload_test_data, get_rest_call, \
    assert_sql_count, CHANNELS_ENDPOINT, BAD_ID


class TestChannel(TestCase):
    def setUp(self) -> None:
        reload_test_data()
        signup_test_member()
        res = login_test_member()

        self.session_key = res.json()['session_key']

        self.channels = fetch_all_channels()

    def test_get(self):
        res = get_rest_call(self, CHANNELS_ENDPOINT,
                            headers={'Session-Key': self.session_key, 'member': TEST_MEMBER['user']})
        assert_sql_count(self, sql="SELECT * FROM channel", n=len(res))

    def test_get_with_id(self):
        channel = self.channels[0]

        res = get_rest_call(self, f'{CHANNELS_ENDPOINT}/{channel["channel_id"]}',
                            headers={'Session-Key': self.session_key, 'member': TEST_MEMBER['user']})
        assert_sql_count(self, "SELECT * FROM message WHERE channel_id = %s", (channel["channel_id"],), len(res))

    def test_get_with_invalid_id(self):
        res = get_rest_call(self, f'{CHANNELS_ENDPOINT}/{BAD_ID}',
                      headers={'Session-Key': self.session_key, 'member': TEST_MEMBER['user']},
                      expected_code=ResCode.CONFLICT.value)

        # Show error message
        print(res)

        assert_sql_count(self, "SELECT * FROM message WHERE channel_id = %s", (BAD_ID,))

    @classmethod
    def tearDownClass(cls) -> None:
        reload_test_data()
