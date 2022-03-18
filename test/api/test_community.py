from unittest import TestCase

from test.utils import reload_test_data, get_rest_call, assert_sql_count

COMMUNITIES_ENDPOINT = 'http://127.0.0.1:5000/communities'


class TestCommunity(TestCase):
    def setUp(self) -> None:
        reload_test_data()

    def test_get(self):
        res = get_rest_call(self, COMMUNITIES_ENDPOINT)
        assert_sql_count(self, sql="SELECT * FROM community", n=len(res))

    @classmethod
    def tearDownClass(cls) -> None:
        reload_test_data()
