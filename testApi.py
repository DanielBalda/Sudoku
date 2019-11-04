import unittest
from unittest.mock import MagicMock, patch
from parameterized import parameterized
from api import (
    Api,
    ApiNotRespond,
)


class TestSudoku(unittest.TestCase):
    @parameterized.expand([
        ([{"response":"true","size":"9","squares":[{"x":0,"y":0,"value":5},{"x":0,"y":1,"value":3},{"x":0,"y":3,"value":7},{"x":0,"y":6,"value":8},{"x":0,"y":8,"value":6},{"x":1,"y":0,"value":4},{"x":1,"y":4,"value":1},{"x":1,"y":5,"value":2},{"x":1,"y":6,"value":7},{"x":2,"y":1,"value":7},{"x":2,"y":3,"value":5},{"x":2,"y":5,"value":8},{"x":2,"y":6,"value":4},{"x":2,"y":7,"value":3},{"x":3,"y":0,"value":1},{"x":3,"y":1,"value":8},{"x":3,"y":4,"value":2},{"x":3,"y":7,"value":4},{"x":4,"y":2,"value":7},{"x":4,"y":3,"value":4},{"x":4,"y":4,"value":8},{"x":4,"y":5,"value":1},{"x":4,"y":6,"value":3},{"x":5,"y":1,"value":2},{"x":5,"y":2,"value":4},{"x":5,"y":4,"value":5},{"x":5,"y":6,"value":6},{"x":5,"y":7,"value":8},{"x":6,"y":1,"value":1},{"x":6,"y":2,"value":3},{"x":6,"y":3,"value":8},{"x":6,"y":5,"value":6},{"x":6,"y":7,"value":7},{"x":7,"y":2,"value":6},{"x":7,"y":3,"value":2},{"x":7,"y":4,"value":3},{"x":7,"y":8,"value":8},{"x":8,"y":0,"value":8},{"x":8,"y":2,"value":9},{"x":8,"y":7,"value":6},{"x":8,"y":8,"value":3}]}], "53■7■■8■64■■■127■■■7■5■843■18■■2■■4■■■74813■■■24■5■68■■138■6■7■■■623■■■88■9■■■■63"),
        ([{"response":"true","size":"9","squares":[{"x":0,"y":0,"value":7},{"x":0,"y":1,"value":5},{"x":0,"y":4,"value":3},{"x":0,"y":6,"value":4},{"x":0,"y":7,"value":9},{"x":1,"y":1,"value":2},{"x":1,"y":2,"value":4},{"x":1,"y":4,"value":5},{"x":1,"y":7,"value":6},{"x":2,"y":2,"value":1},{"x":2,"y":3,"value":6},{"x":2,"y":6,"value":2},{"x":2,"y":8,"value":7},{"x":3,"y":0,"value":6},{"x":3,"y":2,"value":7},{"x":3,"y":6,"value":8},{"x":3,"y":8,"value":5},{"x":4,"y":0,"value":4},{"x":4,"y":1,"value":3},{"x":4,"y":3,"value":5},{"x":4,"y":5,"value":6},{"x":4,"y":8,"value":9},{"x":5,"y":0,"value":5},{"x":5,"y":2,"value":8},{"x":5,"y":3,"value":1},{"x":5,"y":6,"value":3},{"x":5,"y":8,"value":6},{"x":6,"y":1,"value":4},{"x":6,"y":3,"value":7},{"x":6,"y":4,"value":6},{"x":6,"y":7,"value":8},{"x":7,"y":0,"value":2},{"x":7,"y":2,"value":5},{"x":7,"y":4,"value":1},{"x":7,"y":8,"value":4},{"x":8,"y":1,"value":6},{"x":8,"y":3,"value":4},{"x":8,"y":4,"value":2},{"x":8,"y":6,"value":5},{"x":8,"y":7,"value":7},{"x":8,"y":8,"value":1}]}], "75■■3■49■■24■5■■6■■■16■■2■76■7■■■8■543■5■6■■95■81■■3■6■4■76■■8■2■5■1■■■4■6■42■571"),
        ([{"response":"true","size":"9","squares":[{"x":0,"y":2,"value":1},{"x":0,"y":3,"value":7},{"x":0,"y":6,"value":6},{"x":0,"y":8,"value":8},{"x":1,"y":0,"value":4},{"x":1,"y":1,"value":6},{"x":1,"y":4,"value":5},{"x":1,"y":6,"value":3},{"x":1,"y":8,"value":1},{"x":2,"y":2,"value":8},{"x":2,"y":4,"value":6},{"x":2,"y":8,"value":2},{"x":3,"y":1,"value":1},{"x":3,"y":4,"value":9},{"x":3,"y":6,"value":8},{"x":3,"y":8,"value":4},{"x":4,"y":0,"value":8},{"x":4,"y":1,"value":7},{"x":4,"y":3,"value":2},{"x":4,"y":4,"value":3},{"x":4,"y":7,"value":6},{"x":5,"y":0,"value":6},{"x":5,"y":1,"value":5},{"x":5,"y":2,"value":9},{"x":5,"y":3,"value":4},{"x":5,"y":4,"value":7},{"x":6,"y":0,"value":2},{"x":6,"y":1,"value":9},{"x":6,"y":3,"value":6},{"x":6,"y":6,"value":1},{"x":6,"y":7,"value":3},{"x":7,"y":0,"value":1},{"x":7,"y":3,"value":9},{"x":7,"y":4,"value":2},{"x":7,"y":6,"value":5},{"x":7,"y":7,"value":8},{"x":7,"y":8,"value":6},{"x":8,"y":2,"value":6},{"x":8,"y":5,"value":5},{"x":8,"y":6,"value":4}]}], "■■17■■6■846■■5■3■1■■8■6■■■2■1■■9■8■487■23■■6■65947■■■■29■6■■13■1■■92■586■■6■■54■■"),
        ([{"response":"true","size":"9","squares":[{"x":0,"y":0,"value":6},{"x":0,"y":1,"value":3},{"x":0,"y":6,"value":9},{"x":0,"y":8,"value":1},{"x":1,"y":1,"value":5},{"x":1,"y":2,"value":1},{"x":1,"y":5,"value":7},{"x":1,"y":7,"value":4},{"x":1,"y":8,"value":2},{"x":2,"y":2,"value":9},{"x":2,"y":3,"value":1},{"x":2,"y":4,"value":3},{"x":2,"y":5,"value":5},{"x":2,"y":6,"value":8},{"x":3,"y":0,"value":2},{"x":3,"y":1,"value":9},{"x":3,"y":2,"value":3},{"x":3,"y":6,"value":7},{"x":4,"y":1,"value":7},{"x":4,"y":3,"value":2},{"x":4,"y":4,"value":4},{"x":4,"y":5,"value":3},{"x":4,"y":8,"value":6},{"x":5,"y":0,"value":1},{"x":5,"y":1,"value":6},{"x":5,"y":3,"value":7},{"x":5,"y":5,"value":9},{"x":6,"y":2,"value":2},{"x":6,"y":3,"value":6},{"x":6,"y":4,"value":5},{"x":6,"y":5,"value":1},{"x":6,"y":6,"value":4},{"x":6,"y":7,"value":7},{"x":7,"y":1,"value":4},{"x":7,"y":2,"value":5},{"x":7,"y":7,"value":1},{"x":7,"y":8,"value":3},{"x":8,"y":0,"value":9},{"x":8,"y":3,"value":3},{"x":8,"y":6,"value":5},{"x":8,"y":8,"value":8}]}], "63■■■■9■1■51■■7■42■■91358■■293■■■7■■■7■243■■616■7■9■■■■■265147■■45■■■■139■■3■■5■8")
    ])
    def test_api_9x9(self, jsonResp, result):
        mock = MagicMock()
        mock.json = MagicMock(return_value=jsonResp[0])
        mock.status_code = 200
        with patch("api.requests.get", return_value=mock):
            apiResponse = Api(9).request()
        self.assertEqual(apiResponse, result)

    @parameterized.expand([
        ([{"response":"true","size":"4","squares":[{"x":0,"y":1,"value":3},{"x":0,"y":2,"value":4},{"x":1,"y":1,"value":4},{"x":1,"y":2,"value":3},{"x":2,"y":1,"value":2},{"x":2,"y":2,"value":1},{"x":3,"y":0,"value":3},{"x":3,"y":3,"value":4}]}], "■34■■43■■21■3■■4"),
        ([{"response":"true","size":"4","squares":[{"x":0,"y":0,"value":4},{"x":0,"y":1,"value":2},{"x":0,"y":2,"value":3},{"x":1,"y":2,"value":2},{"x":1,"y":3,"value":4},{"x":2,"y":2,"value":4},{"x":2,"y":3,"value":3},{"x":3,"y":1,"value":4},{"x":3,"y":3,"value":2}]}], "423■■■24■■43■4■2"),
        ([{"response":"true","size":"4","squares":[{"x":0,"y":0,"value":3},{"x":0,"y":2,"value":2},{"x":1,"y":1,"value":2},{"x":1,"y":3,"value":4},{"x":2,"y":2,"value":4},{"x":2,"y":3,"value":3},{"x":3,"y":0,"value":4},{"x":3,"y":2,"value":1}]}], "3■2■■2■4■■434■1■"),
        ([{"response":"true","size":"4","squares":[{"x":0,"y":1,"value":2},{"x":0,"y":2,"value":1},{"x":0,"y":3,"value":4},{"x":1,"y":2,"value":2},{"x":2,"y":1,"value":3},{"x":3,"y":1,"value":1},{"x":3,"y":2,"value":3},{"x":3,"y":3,"value":2}]}], "■214■■2■■3■■■132")
    ])
    def test_api_4x4(self, jsonResp, result):
        mock = MagicMock()
        mock.json = MagicMock(return_value=jsonResp[0])
        mock.status_code = 200
        with patch("api.requests.get", return_value=mock):
            apiResponse = Api(4).request()
        self.assertEqual(apiResponse, result)

    def test_api_not_respond(self):
        mock = MagicMock()
        mock.status_code = 408 #Timeout
        with patch("api.requests.get", return_value=mock):
            with self.assertRaises(ApiNotRespond):
                apiResponse = Api(4).request()

    def test_api_not_found(self):
        mock = MagicMock()
        mock.status_code = 404 #NotFound
        with patch("api.requests.get", return_value=mock):
            with self.assertRaises(ApiNotRespond):
                apiResponse = Api(9).request()

if __name__ == "__main__":
    unittest.main()