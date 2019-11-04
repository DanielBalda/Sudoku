import unittest
from parameterized import parameterized
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

    @parameterized.expand([
        ('f', '5', '3'),
        ('A', '5', '3'),
        ('j', '5', '3'),
        ('W', '5', '3'),
        ('S', '5', '3'),
        ('o', '5', '3')
    ])
    def test_put_letter_in_number(self, number, x, y):
        with self.assertRaises(InputChar):
            self.interface.validateNumber(number, x, y)

    @parameterized.expand([
        ('5', 'X', '3'),
        ('5', 'm', '3'),
        ('5', 'l', '3'),
        ('5', 's', '3'),
        ('5', 'J', '3'),
        ('5', 'O', '3')
    ])
    def test_put_letter_in_x(self, number, x, y):
        with self.assertRaises(InputChar):
            self.interface.validateNumber(number, x, y)

    @parameterized.expand([
        ('5', '2', 'D'),
        ('5', '2', 'C'),
        ('5', '2', 'a'),
        ('5', '2', 'h'),
        ('5', '2', 'g'),
        ('5', '2', 'w')
    ])
    def test_put_letter_in_y(self, number, x, y):
        with self.assertRaises(InputChar):
            self.interface.validateNumber(number, x, y)

    @parameterized.expand([
        ('/', '5', '3'),
        ('%', '5', '3'),
        ('#', '5', '3'),
        ('$', '5', '3'),
        ('(', '5', '3'),
        ('!', '5', '3')
    ])
    def test_put_symbol_in_number(self, number, x, y):
        with self.assertRaises(InputSymbol):
            self.interface.validateNumber(number, x, y)

    @parameterized.expand([
        ('5', ']', '3'),
        ('5', ';', '3'),
        ('5', '@', '3'),
        ('5', '&', '3'),
        ('5', '$', '3'),
        ('5', '*', '3')
    ])
    def test_put_symbol_in_x(self, number, x, y):
        with self.assertRaises(InputSymbol):
            self.interface.validateNumber(number, x, y)

    @parameterized.expand([
        ('5', '3', '*'),
        ('5', '3', '&'),
        ('5', '3', '%'),
        ('5', '3', '$'),
        ('5', '3', '#'),
        ('5', '3', '@')
    ])
    def test_put_symbol_in_y(self, number, x, y):
        with self.assertRaises(InputSymbol):
            self.interface.validateNumber(number, x, y)

    @parameterized.expand([
        ('50', '