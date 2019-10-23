import unittest
from interface import Interface


class TestInterface(unittest.TestCase):

    def test_put_letter_in_number(self):
        self.assertEqual(self.Interface.play(), "Ups! Server not respond.")

    def test_put_letter_in_x(self):
        self.assertEqual(self.Interface.play(), "Ups! Server not respond.")

    def test_put_letter_in_y(self):
        self.assertEqual(self.Interface.play(), "Ups! Server not respond.")

    def test_api_invalid_size(self):
        self.assertEqual(self.Interface.play(), "Ups! Server not respond.")


if __name__ == "__main__":
    unittest.main()
