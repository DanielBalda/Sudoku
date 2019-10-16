import unittest
from sudoku import Sudoku


class TestSudoku(unittest.TestCase):

    def test_put_number_1(self):
        sudoku = Sudoku("53XX7XXXX6XX195XXXX98XXXX6X8XXX6XXX34XX8X3XX17XXX2XXX6X6XXXX28XXXX419XX5XXXX8XX79")
        self.assertTrue(sudoku.putNumber(3, 2, 4))

    def test_put_number_2(self):
        sudoku = Sudoku("53XX7XXXX6XX195XXXX98XXXX6X8XXX6XXX34XX8X3XX17XXX2XXX6X6XXXX28XXXX419XX5XXXX8XX79")
        self.assertFalse(sudoku.putNumber(3, 3, 4))

    def test_put_number_3(self):
        sudoku = Sudoku("53XX7XXXX6XX195XXXX98XXXX6X8XXX6XXX34XX8X3XX17XXX2XXX6X6XXXX28XXXX419XX5XXXX8XX79")
        self.assertFalse(sudoku.putNumber(1, 7, 8))

    def test_put_number_4(self):
        sudoku = Sudoku("53XX7XXXX6XX195XXXX98XXXX6X8XXX6XXX34XX8X3XX17XXX2XXX6X6XXXX28XXXX419XX5XXXX8XX79")
        self.assertFalse(sudoku.putNumber(6, 4, 7))

    def test_put_number_5(self):
        sudoku = Sudoku("53XX7XXXX6XX195XXXX98XXXX6X8XXX6XXX34XX8X3XX17XXX2XXX6X6XXXX28XXXX419XX5XXXX8XX79")
        self.assertTrue(sudoku.putNumber(3, 2, 4))

    def test_put_number_exist_in_region(self):
        sudoku = Sudoku("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX7X")
        self.assertFalse(sudoku.putNumber(7, 7, 6))

    def test_game_not_over(self):
        sudoku = Sudoku("53XX7XXXX6XX195XXXX98XXXX6X8XXX6XXX34XX8X3XX17XXX2XXX6X6XXXX28XXXX419XX5XXXX8XX79")
        over = sudoku.isOver()
        self.assertFalse(over)

    def test_game_not_over_2(self):
        sudoku = Sudoku("53XX7XXXX6XX195XX2X98XXXX6X8XXX6XXX34XX8X3XX17XXX2XXX6X6X3XX28XXXX419XX5XXXX8XX79")
        self.assertTrue(sudoku.putNumber(3, 2, 4))
        self.assertTrue(sudoku.putNumber(5, 3, 6))
        self.assertFalse(sudoku.putNumber(1, 5, 8))
        over = sudoku.isOver()
        self.assertFalse(over)

    def test_win_after_last_play(self):
        sudoku = Sudoku("534678912672195348198342567859761423426853791713924856961537284287419635345286X79")
        self.assertTrue(sudoku.putNumber(1, 8, 6))
        over = sudoku.isOver()
        self.assertTrue(over)

    def test_win(self):
        sudoku = Sudoku("534678912672195348198342567859761423426853791713924856961537284287419635345286179")
        over = sudoku.isOver()
        self.assertTrue(over)

    def test_no_win(self):
        sudoku = Sudoku("53XX7X25XX6XX195XXXX98XXXX6X8XXX6XXX34XX8X3XX17XXX2XXX6X6XXXX28XXXX419XX5XXXX8XX79")
        over = sudoku.isOver()
        self.assertFalse(over)


if __name__ == '__main__':
    unittest.main()
