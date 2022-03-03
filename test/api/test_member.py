from unittest import TestCase

from src.db.utils import connect, init_db
from test.utils import reload_test_data, assert_sql_count, get_rest_call


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
        # res = requests.get(self.ENDPOINT)

        get_rest_call(self, self.ENDPOINT)
        assert_sql_count(self, sql="SELECT * FROM member", n=self.ROWS)

        # self.assertEqual(self.SUCCESS, res.status_code)
        # self.assertEqual(self.ROWS, len(res.json()))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.conn.close()
