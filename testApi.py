import unittest
from api import Api


class TestSudoku(unittest.TestCase):

    def test_api_not_respond(self):
        self.assertEqual(Api.request(9), "Ups! Server not respond.")

    def test_api_invalid_size(self):
        self.assertEqual(Api.request(10), "Ups! Server not respond.")


if __name__ == "__main__":
    unittest.main()
