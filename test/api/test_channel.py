from unittest import TestCase

import requests

from src.db.utils import connect, rebuild_tables
from utils import insert_test_data


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

    def setUp(self) -> None:
        rebuild_tables()
        insert_test_data()

    def test_get(self):
        res = requests.get(self.ENDPOINT)

        self.assertEqual(self.SUCCESS, res.status_code)
        self.assertEqual(self.CHAN_ROWS, len(res.json()))

    def test_get_with_id(self):
        self.cur.execute("""
            SELECT channel_id FROM channel WHERE channel_name = %s
        """, ('worms',))

        chan_id = self.cur.fetchone()[0]

        res = requests.get(f'{self.ENDPOINT}/{chan_id}')

        self.assertEqual(self.SUCCESS, res.status_code)
        self.assertEqual(self.MSG_ROWS, len(res.json()))

    def test_get_with_invalid_id(self):
        res = requests.get(f'{self.ENDPOINT}/{self.BAD_ID}')

        self.assertEqual(self.SUCCESS, res.status_code)
        self.assertEqual(self.EMPTY, res.json())
