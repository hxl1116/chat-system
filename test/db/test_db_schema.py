import unittest

from src.db.utils import rebuild_tables
from test.utils import *


class TestDBSchema(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def test_rebuild_tables(self):
        """Rebuild the tables"""
        rebuild_tables()
        assert_sql_count(self, sql="SELECT * FROM community", n=0)

    def test_rebuild_tables_is_idempotent(self):
        """Drop and rebuild the tables twice"""
        rebuild_tables()
        rebuild_tables()
        assert_sql_count(self, sql="SELECT * FROM community", n=0)

    def test_seed_data_works(self):
        """Attempt to insert the seed data"""
        rebuild_tables()
        reload_test_data()
        assert_sql_count(self, sql="SELECT * FROM community", n=2)
