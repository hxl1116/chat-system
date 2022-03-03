from unittest import TestCase

import requests

from src.db.utils import connect, init_db
from test.utils import reload_test_data


class TestMember(TestCase):
    ENDPOINT = 'http://127.0.0.1:5000/members'
    SUCCESS = 200
    ROWS = 7

    conn = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.conn = connect()
        cls.cur = cls.conn.cursor()
        init_db()

    def setUp(self) -> None:
        reload_test_data()

    def test_get(self):
        res = requests.get(self.ENDPOINT)

        self.assertEqual(self.SUCCESS, res.status_code)
        self.assertEqual(self.ROWS, len(res.json()))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.conn.close()
