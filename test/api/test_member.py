from unittest import TestCase

from src.db.member import fetch_all_members
from src.db.utils import connect, init_db
from test.utils import reload_test_data, assert_sql_count, get_rest_call, put_rest_call, post_rest_call, del_rest_call


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
        self.members = fetch_all_members()
        self.params = {
            'last': 'Larson',
            'first': 'Henry',
            'user': 'chicken_wing',
            'email': 'hxl1116@g.rit.edu'
        }

    def test_get(self):
        res = get_rest_call(self, self.ENDPOINT)
        assert_sql_count(self, sql="SELECT * FROM member", n=len(res))

    def test_post(self):
        post_rest_call(self, self.ENDPOINT, data=self.params)

        assert_sql_count(self, sql="SELECT * FROM member", n=len(self.members) + 1)

    def test_put(self):
        member = self.members[0]
        put_rest_call(self, f'{self.ENDPOINT}/{member[0]}', data=self.params)
        assert_sql_count(self, sql="SELECT * FROM member", n=len(self.members))

    def test_delete(self):
        member = self.members[0]
        del_rest_call(self, f'{self.ENDPOINT}/{member[0]}')
        assert_sql_count(self, sql="SELECT * FROM member", n=len(self.members) - 1)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.conn.close()
