import unittest

from src.db.example import rebuild_tables
from test.utils import *


class TestExample(unittest.TestCase):

    def setUp(self):
        rebuild_tables()
        insert_test_data()

    def test_hello_world(self):
        expected = {'1': 'hello, world!'}
        actual = get_rest_call(self, 'http://127.0.0.1:5000')
        self.assertEqual(expected, actual)
