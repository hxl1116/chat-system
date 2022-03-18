from unittest import TestCase

from src.db.channel import fetch_all_channels
from test.utils import reload_test_data, get_rest_call, assert_sql_count

BAD_ID = '00000000-0000-0000-0000-000000000000'
CHANNELS_ENDPOINT = 'http://127.0.0.1:5000/channels'


class TestChannel(TestCase):
    def setUp(self) -> None:
        reload_test_data()

        self.channels = fetch_all_channels()

    def test_get(self):
        res = get_rest_call(self, CHANNELS_ENDPOINT)
        assert_sql_count(self, sql="SELECT * FROM channel", n=len(res))

    def test_get_with_id(self):
        channel = self.channels[0]

        res = get_rest_call(self, f'{CHANNELS_ENDPOINT}/{channel["channel_id"]}')
        assert_sql_count(self, "SELECT * FROM message WHERE channel_id = %s", (channel["channel_id"],), len(res))

    def test_get_with_invalid_id(self):
        res = get_rest_call(self, f'{CHANNELS_ENDPOINT}/{BAD_ID}')
        assert_sql_count(self, "SELECT * FROM message WHERE channel_id = %s", (BAD_ID,))

    @classmethod
    def tearDownClass(cls) -> None:
        reload_test_data()
