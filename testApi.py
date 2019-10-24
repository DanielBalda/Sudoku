import unittest
from unittest.mock import MagicMock, patch
from api import Api


class TestSudoku(unittest.TestCase):

    def test_api_9x9_1(self):
        mock = MagicMock()
        mock.json = MagicMock(return_value={"response":"true","size":"9","squares":[{"x":0,"y":0,"value":5},{"x":0,"y":1,"value":3},{"x":0,"y":3,"value":7},{"x":0,"y":6,"value":8},{"x":0,"y":8,"value":6},{"x":1,"y":0,"value":4},{"x":1,"y":4,"value":1},{"x":1,"y":5,"value":2},{"x":1,"y":6,"value":7},{"x":2,"y":1,"value":7},{"x":2,"y":3,"value":5},{"x":2,"y":5,"value":8},{"x":2,"y":6,"value":4},{"x":2,"y":7,"value":3},{"x":3,"y":0,"value":1},{"x":3,"y":1,"value":8},{"x":3,"y":4,"value":2},{"x":3,"y":7,"value":4},{"x":4,"y":2,"value":7},{"x":4,"y":3,"value":4},{"x":4,"y":4,"value":8},{"x":4,"y":5,"value":1},{"x":4,"y":6,"value":3},{"x":5,"y":1,"value":2},{"x":5,"y":2,"value":4},{"x":5,"y":4,"value":5},{"x":5,"y":6,"value":6},{"x":5,"y":7,"value":8},{"x":6,"y":1,"value":1},{"x":6,"y":2,"value":3},{"x":6,"y":3,"value":8},{"x":6,"y":5,"value":6},{"x":6,"y":7,"value":7},{"x":7,"y":2,"value":6},{"x":7,"y":3,"value":2},{"x":7,"y":4,"value":3},{"x":7,"y":8,"value":8},{"x":8,"y":0,"value":8},{"x":8,"y":2,"value":9},{"x":8,"y":7,"value":6},{"x":8,"y":8,"value":3}]})
        mock.status_code = mock.PropertyMock(return_value=200)
        with patch("api.requests.get", return_value=mock):
            apiResponse = Api(9).request()
        self.assertEqual(apiResponse, "53■7■■8■64■■■127■■■7■5■843■18■■2■■4■■■74813■■■24■5■68■■138■6■7■■■623■■■88■9■■■■63")

    def test_api_9x9_2(self):
        mock = MagicMock()
        mock.json = MagicMock(return_value={"response":"true","size":"9","squares":[{"x":0,"y":1,"value":2},{"x":0,"y":2,"value":5},{"x":0,"y":4,"value":8},{"x":0,"y":6,"value":6},{"x":0,"y":7,"value":4},{"x":1,"y":0,"value":6},{"x":1,"y":2,"value":3},{"x":1,"y":3,"value":7},{"x":1,"y":4,"value":4},{"x":1,"y":5,"value":9},{"x":2,"y":0,"value":4},{"x":2,"y":6,"value":1},{"x":2,"y":8,"value":3},{"x":3,"y":1,"value":6},{"x":3,"y":2,"value":2},{"x":3,"y":5,"value":7},{"x":3,"y":7,"value":5},{"x":3,"y":8,"value":1},{"x":4,"y":1,"value":5},{"x":4,"y":2,"value":4},{"x":4,"y":3,"value":6},{"x":4,"y":5,"value":8},{"x":4,"y":6,"value":2},{"x":5,"y":0,"value":8},{"x":5,"y":1,"value":7},{"x":5,"y":4,"value":1},{"x":5,"y":6,"value":3},{"x":5,"y":7,"value":6},{"x":6,"y":2,"value":1},{"x":6,"y":3,"value":8},{"x":6,"y":5,"value":6},{"x":7,"y":1,"value":9},{"x":7,"y":3,"value":3},{"x":7,"y":4,"value":5},{"x":7,"y":5,"value":1},{"x":7,"y":6,"value":4},{"x":7,"y":8,"value":2},{"x":8,"y":4,"value":2},{"x":8,"y":6,"value":7},{"x":8,"y":8,"value":6}]})
        with patch("api.requests.get", return_value=mock):
            apiResponse = Api(9).request()
        self.assertEqual(apiResponse, "■25■8■64■6■3749■■■4■■■■■1■3■62■■7■51■546■82■■87■■1■36■■■18■6■■■■9■3514■2■■■■2■7■6")

    def test_api_4x4_1(self):
        mock = MagicMock()
        mock.json = MagicMock(return_value={"response":"true","size":"4","squares":[{"x":0,"y":0,"value":3},{"x":0,"y":1,"value":2},{"x":1,"y":1,"value":4},{"x":1,"y":2,"value":2},{"x":1,"y":3,"value":3},{"x":2,"y":0,"value":4},{"x":2,"y":1,"value":1},{"x":2,"y":2,"value":3}]})
        with patch("api.requests.get", return_value=mock):
            apiResponse = Api(4).request()
        self.assertEqual(apiResponse, "32■■■423413■■■■■")

    def test_api_4x4_2(self):
        mock = MagicMock()
        mock.json = MagicMock(return_value={"response":"true","size":"4","squares":[{"x":0,"y":0,"value":2},{"x":0,"y":3,"value":4},{"x":1,"y":1,"value":4},{"x":1,"y":2,"value":2},{"x":2,"y":1,"value":2},{"x":2,"y":2,"value":1},{"x":2,"y":3,"value":3},{"x":3,"y":0,"value":1},{"x":3,"y":3,"value":2}]})
        with patch("api.requests.get", return_value=mock):
            apiResponse = Api(4).request()
        self.assertEqual(apiResponse, "2■■4■42■■2131■■2")


if __name__ == "__main__":
    unittest.main()
