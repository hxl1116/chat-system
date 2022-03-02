from unittest import TestCase

import requests


class TestMember(TestCase):
    ENDPOINT = 'http://127.0.0.1:5000/members'
    SUCCESS = 200
    ROWS = 7

    def test_get(self):
        res = requests.get(self.ENDPOINT)

        self.assertEqual(self.SUCCESS, res.status_code)
        self.assertEqual(self.ROWS, len(res.json()))
