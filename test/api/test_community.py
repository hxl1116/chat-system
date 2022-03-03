import unittest
from unittest import TestCase

import requests

from src.db.utils import connect, rebuild_tables
from test.utils import reload_test_data


class TestCommunity(TestCase):
    ENDPOINT = 'http://127.0.0.1:5000/communities'
    SUCCESS = 200
    ROWS = 2

    conn = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.conn = connect()
        cls.cur = cls.conn.cursor()
        rebuild_tables()

    def setUp(self) -> None:
        reload_test_data()
        self.conn.commit()

    def test_get(self):
        res = requests.get(self.ENDPOINT)

        # get_rest_call(self, self.ENDPOINT)
        # assert_sql_count(self, sql="SELECT * FROM community", n=self.ROWS)

        self.assertEqual(self.SUCCESS, res.status_code)
        self.assertEqual(self.ROWS, len(res.json()))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.conn.close()