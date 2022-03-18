import unittest
from unittest import TestCase

from src.db.member import update_member
from src.db.utils import connect, init_db, fetch_many
from test.utils import reload_test_data


# TODO: Implement tests
class TestMember(TestCase):
    conn = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.conn = connect()
        cls.cur = cls.conn.cursor()
        init_db()

    def setUp(self) -> None:
        reload_test_data()

        self.members = fetch_many("""
            SELECT * FROM member
        """)

    @unittest.skip('not implemented')
    def test_member_exists(self):
        pass

    @unittest.skip('not implemented')
    def test_fetch_member_id(self):
        pass

    @unittest.skip('not implemented')
    def test_fetch_all_members(self):
        pass

    @unittest.skip('not implemented')
    def test_insert_member(self):
        pass

    def test_update_member(self):
        test_data = {
            'id': self.members[0]['member_id'],
            'last_name': 'Larson',
            'first_name': 'Henry',
            'username': 'chicken_wing',
            'email': 'hxl1116@g.rit.edu'
        }

        update_member(**test_data)

    @unittest.skip('not implemented')
    def test_delete_member(self):
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.conn.close()
