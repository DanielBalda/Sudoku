import unittest
from interface import (
    Interface,
    EmptyVar,
    InvalidNumber,
    InputChar,
    InputSymbol
)


class TestInterface(unittest.TestCase):
    def setUp(self):
        self.interface = Interface()
        self.interface.boardSize = 9

    def test_put_letter_in_number(self):
        with self.assertRaises(InputChar):
            self.interface.validateNumber('f', '5', '3')

    def test_put_letter_in_x(self):
        with self.assertRaises(InputChar):
            self.interface.validateNumber('5', 'j', '0')

    def test_put_letter_in_y(self):
        with self.assertRaises(InputChar):
            self.interface.validateNumber('5', '2', 'w')

    def test_put_symbol_in_number(self):
        with self.assertRaises(InputSymbol):
            self.interface.validateNumber('/', '5', '3')

    def test_put_symbol_in_x(self):
        with self.assertRaises(InputSymbol):
            self.interface.validateNumber('5', ']', '0')

    def test_put_symbol_in_y(self):
        with self.assertRaises(InputSymbol):
            self.interface.validateNumber('5', '@', 'w')

    def test_put_big_number(self):
        with self.assertRaises(InvalidNumber):
            self.interface.validateNumber('18', '4', '2')

    def test_put_negative_number(self):
        with self.assertRaises(InvalidNumber):
            self.interface.validateNumber('-8', '4', '2')

    def test_put_blak(self):
        with self.assertRaises(EmptyVar):
            self.interface.validateNumber('', '4', '2')

    def test_put_valid_number_9x9(self):
        self.assertTrue(self.interface.validateNumber('8', '3', '6'))

    def test_put_valid_number_in_x_9x9(self):
        self.assertTrue(self.interface.validateNumber('2', '5', '2'))

    def test_put_valid_number_in_y_9x9(self):
        self.assertTrue(self.interface.validateNumber('1', '3', '6'))

    def test_put_valid_number_4x4(self):
        self.interface.boardSize = 4
        self.assertTrue(self.interface.validateNumber('7', '3', '1'))

    def test_put_valid_number_in_x_4x4(self):
        self.interface.boardSize = 4
        self.assertTrue(self.interface.validateNumber('2', '1', '2'))

    def test_put_valid_number_in_y_4x4(self):
        self.interface.boardSize = 4
        self.assertTrue(self.interface.validateNumber('9', '3', '3'))


if __name__ == "__main__":
    unittest.main()
