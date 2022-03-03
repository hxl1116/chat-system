from unittest import TestCase

import requests

from src.db.utils import connect, rebuild_tables
from utils import insert_test_data


class TestCommunity(TestCase):
    ENDPOINT = 'http://127.0.0.1:5000/communities'
    SUCCESS = 200
    ROWS = 2

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
        self.assertEqual(self.ROWS, len(res.json()))
