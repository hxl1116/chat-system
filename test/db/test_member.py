from unittest import TestCase

from src.db.utils import connect, init_db
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

    def test_member_exists(self):
        pass

    def test_fetch_member_id(self):
        pass

    def test_fetch_all_members(self):
        pass

    def test_insert_member(self):
        pass

    def test_update_member(self):
        pass

    def test_delete_member(self):
        pass

    def tearDown(self) -> None:
        pass
