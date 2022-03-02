from unittest import TestCase

import requests


class TestCommunity(TestCase):
    ENDPOINT = 'http://127.0.0.1:5000/communities'
    SUCCESS = 200
    ROWS = 2

    def test_get(self):
        res = requests.get(self.ENDPOINT)

        self.assertEqual(self.SUCCESS, res.status_code)
        self.assertEqual(self.ROWS, len(res.json()))
