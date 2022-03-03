from unittest import TestCase

from src.db.utils import connect, rebuild_tables, init_db
from test.utils import reload_test_data, get_rest_call, assert_sql_count


class TestChannel(TestCase):
    BAD_ID = '00000000-0000-0000-0000-000000000000'
    ENDPOINT = 'http://127.0.0.1:5000/channels'
    SUCCESS = 200
    CHAN_ROWS = 4
    MSG_ROWS = 3
    EMPTY = []

    conn = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.conn = connect()
        cls.cur = cls.conn.cursor()
        init_db()

    def setUp(self) -> None:
        reload_test_data()

    def test_get(self):
        get_rest_call(self, self.ENDPOINT)
        assert_sql_count(self, sql="SELECT * FROM channel", n=self.CHAN_ROWS)

    def test_get_with_id(self):
        self.cur.execute("""
            SELECT channel_id FROM channel WHERE channel_name = %s
        """, ('worms',))
        chan_id = self.cur.fetchone()[0]

        get_rest_call(self, f'{self.ENDPOINT}/{chan_id}')
        assert_sql_count(self, "SELECT * FROM message WHERE channel_id = %s", (chan_id,), self.MSG_ROWS)

    def test_get_with_invalid_id(self):
        get_rest_call(self, f'{self.ENDPOINT}/{self.BAD_ID}')
        assert_sql_count(self, "SELECT * FROM message WHERE channel_id = %s", (self.BAD_ID,))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.conn.close()
