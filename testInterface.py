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
        ('50', '5', '3'),
        ('49', '5', '3'),
        ('999', '5', '3'),
        ('85', '5', '3'),
        ('12', '5', '3'),
        ('33', '5', '3')
    ])
    def test_put_big_number(self, number, x, y):
        with self.assertRaises(InvalidNumber):
            self.interface.validateNumber(number, x, y)

    @parameterized.expand([
        ('-50', '5', '3'),
        ('-49', '5', '3'),
        ('-999', '5', '3'),
        ('-85', '5', '3'),
        ('-12', '5', '3'),
        ('-33', '5', '3')
    ])
    def test_put_negative_number(self, number, x, y):
        with self.assertRaises(InvalidNumber):
            self.interface.validateNumber(number, x, y)

    def test_put_blank(self):
        with self.assertRaises(EmptyVar):
            self.interface.validateNumber('', '4', '2')

    # NUMEROS VALIDOS

    @parameterized.expand([
        ('8', '3', '6'),
        ('6', '2', '8')
    ])
    def test_put_valid_number_9x9(self, number, x, y):
        self.assertTrue(self.interface.validateNumber(number, x, y))

    @parameterized.expand([
        ('2', '5', '2'),
        ('1', '8', '8')
    ])
    def test_put_valid_number_in_x_9x9(self, number, x, y):
        self.assertTrue(self.interface.validateNumber(number, x, y))

    @parameterized.expand([
        ('8', '3', '3'),
        ('6', '2', '5')
    ])
    def test_put_valid_number_in_y_9x9(self, number, x, y):
        self.assertTrue(self.interface.validateNumber(number, x, y))

    @parameterized.expand([
        ('2', '3', '3'),
        ('1', '2', '1')
    ])
    def test_put_valid_number_4x4(self, number, x, y):
        self.interface.boardSize = 4
        self.assertTrue(self.interface.validateNumber(number, x, y))

    @parameterized.expand([
        ('2', '3', '0'),
        ('4', '2', '3')
    ])
    def test_put_valid_number_in_x_4x4(self, number, x, y):
        self.interface.boardSize = 4
        self.assertTrue(self.interface.validateNumber(number, x, y))

    @parameterized.expand([
        ('4', '3', '3'),
        ('3', '2', '0')
    ])
    def test_put_valid_number_in_y_4x4(self, number, x, y):
        self.interface.boardSize = 4
        self.assertTrue(self.interface.validateNumber(number, x, y))

    # NUMEROS INVALIDOS

    @parameterized.expand([
        ('82', '3', '6'),
        ('-6', '2', '8')
    ])
    def test_put_invalid_number_9x9(self, number, x, y):
        with self.assertRaises(InvalidNumber):
            self.interface.validateNumber(number, x, y)

    @parameterized.expand([
        ('2', '-5', '2'),
        ('1', '18', '8')
    ])
    def test_put_invalid_number_in_x_9x9(self, number, x, y):
        with self.assertRaises(InvalidNumber):
            self.interface.validateNumber(number, x, y)

    @parameterized.expand([
        ('8', '3', '32'),
        ('6', '2', '-15')
    ])
    def test_put_invalid_number_in_y_9x9(self, number, x, y):
        with self.assertRaises(InvalidNumber):
            self.interface.validateNumber(number, x, y)

    @parameterized.expand([
        ('0', '3', '3'),
        ('12', '2', '1')
    ])
    def test_put_invalid_number_4x4(self, number, x, y):
        self.interface.boardSize = 4
        with self.assertRaises(InvalidNumber):
            self.interface.validateNumber(number, x, y)

    @parameterized.expand([
        ('9', '-2', '0'),
        ('4', '4', '3')
    ])
    def test_put_invalid_number_in_x_4x4(self, number, x, y):
        self.interface.boardSize = 4
        with self.assertRaises(InvalidNumber):
            self.interface.validateNumber(number, x, y)

    @parameterized.expand([
        ('8', '3', '5'),
        ('6', '2', '7')
    ])
    def test_put_invalid_number_in_y_4x4(self, number, x, y):
        self.interface.boardSize = 4
        with self.assertRaises(InvalidNumber):
            self.interface.validateNumber(number, x, y)


if __name__ == "__main__":
    unittest.main()
