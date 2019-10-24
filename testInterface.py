import unittest
from interface import Interface


class TestInterface(unittest.TestCase):

    def test_put_letter_in_number(self):
        interface = Interface()
        self.assertFalse(interface.validateNumber('f', 0, 0))

    def test_put_letter_in_x(self):
        interface = Interface()
        self.assertFalse(interface.validateNumber(5, 'j', 0))

    def test_put_letter_in_y(self):
        interface = Interface()
        self.assertFalse(interface.validateNumber(5, 2, 'w'))

    def test_put_symbol_in_number(self):
        interface = Interface()
        self.assertFalse(interface.validateNumber('=', 4, 2))

    def test_put_symbol_in_x(self):
        interface = Interface()
        self.assertFalse(interface.validateNumber(5, ']', 2))

    def test_put_symbol_in_y(self):
        interface = Interface()
        self.assertFalse(interface.validateNumber(5, 2, '?'))

    def test_put_big_number(self):
        interface = Interface()
        self.assertFalse(interface.validateNumber(18, 4, 2))

    def test_put_negative_number(self):
        interface = Interface()
        self.assertFalse(interface.validateNumber(-8, 4, 2))

    def test_put_blak(self):
        interface = Interface()
        self.assertFalse(interface.validateNumber('', 4, 2))

    def test_put_valid_number_9x9(self):
        interface = Interface()
        interface.boardSize = 9
        self.assertTrue(interface.validateNumber(8, 3, 6))

    def test_put_valid_number_in_x_9x9(self):
        interface = Interface()
        interface.boardSize = 9
        self.assertTrue(interface.validateNumber(2, 5, 2))

    def test_put_valid_number_in_y_9x9(self):
        interface = Interface()
        interface.boardSize = 9
        self.assertTrue(interface.validateNumber(1, 3, 6))

    def test_put_valid_number_4x4(self):
        interface = Interface()
        interface.boardSize = 4
        self.assertTrue(interface.validateNumber(7, 3, 1))

    def test_put_valid_number_in_x_4x4(self):
        interface = Interface()
        interface.boardSize = 4
        self.assertTrue(interface.validateNumber(2, 1, 2))

    def test_put_valid_number_in_y_4x4(self):
        interface = Interface()
        interface.boardSize = 4
        self.assertTrue(interface.validateNumber(9, 3, 3))


if __name__ == "__main__":
    unittest.main()
