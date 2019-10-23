import unittest
from sudoku import Sudoku


class TestSudoku(unittest.TestCase):

    def test_put_number_1(self):
        sudoku = Sudoku("53■■7■■■■"
                        "6■■195■■■"
                        "■98■■■■6■"
                        "8■■■6■■■3"
                        "4■■8■3■■1"
                        "7■■■2■■■6"
                        "■6■■■■28■"
                        "■■■419■■5"
                        "■■■■8■■79")
        self.assertTrue(sudoku.putNumber(3, 2, 4))

    def test_put_number_2(self):
        sudoku = Sudoku("53■■7■■■■"
                        "6■■195■■■"
                        "■98■■■■6■"
                        "8■■■6■■■3"
                        "4■■8■3■■1"
                        "7■■■2■■■6"
                        "■6■■■■28■"
                        "■■■419■■5"
                        "■■■■8■■79")
        self.assertTrue(sudoku.putNumber(8, 0, 8))

    def test_put_number_3(self):
        sudoku = Sudoku("53■■7■■■■"
                        "6■■195■■■"
                        "■98■■■■6■"
                        "8■■■6■■■3"
                        "4■■8■3■■1"
                        "7■■■2■■■6"
                        "■6■■■■28■"
                        "■■■419■■5"
                        "■■■■8■■79")
        self.assertTrue(sudoku.putNumber(1, 8, 0))

    def test_number_exist_in_row(self):
        sudoku = Sudoku("53■■7■■■■"
                        "6■■195■■■"
                        "■98■■■■6■"
                        "8■■■6■■■3"
                        "4■■8■3■■1"
                        "7■■■2■■■6"
                        "■6■■■■28■"
                        "■■■419■■5"
                        "■■■■8■■79")
        self.assertFalse(sudoku.putNumber(5, 0, 7))

    def test_number_exist_in_column(self):
        sudoku = Sudoku("53■■7■■■■"
                        "6■■195■■■"
                        "■98■■■■6■"
                        "8■■■6■■■3"
                        "4■■8■3■■1"
                        "7■■■2■■■6"
                        "■6■■■■28■"
                        "■■■419■■5"
                        "■■■■8■■79")
        self.assertFalse(sudoku.putNumber(9, 0, 8))

    def test_number_exist_in_region(self):
        sudoku = Sudoku("■■■■■■■■■"
                        "■■■■■■■■■"
                        "■■■■■■■■■"
                        "■■■■■■■■■"
                        "■■■■■■■■■"
                        "■■■■■■■■■"
                        "■■■■■■■■■"
                        "■■■■■■■■■"
                        "■■■■■■■7■")
        self.assertFalse(sudoku.putNumber(7, 6, 6))

    def test_game_not_over(self):
        sudoku = Sudoku("53■■7■■■■"
                        "6■■195■■■"
                        "■98■■■■6■"
                        "8■■■6■■■3"
                        "4■■8■3■■1"
                        "7■■■2■■■6"
                        "■6■■■■28■"
                        "■■■419■■5"
                        "■■■■8■■79")
        over = sudoku.isOver()
        self.assertFalse(over)

    def test_game_not_over_2(self):
        sudoku = Sudoku("53■■7■■■■"
                        "6■■195■■2"
                        "■98■■■■6■"
                        "8■■■6■■■3"
                        "4■■8■3■■1"
                        "7■■■2■■■6"
                        "■6■3■■28■"
                        "■■■419■■5"
                        "■■■■8■■79")
        self.assertTrue(sudoku.putNumber(3, 2, 4))
        self.assertTrue(sudoku.putNumber(5, 3, 6))
        self.assertFalse(sudoku.putNumber(1, 5, 8))
        self.assertTrue(sudoku.putNumber(3, 2, 4))
        over = sudoku.isOver()
        self.assertFalse(over)

    def test_win_after_last_play(self):
        sudoku = Sudoku("534678912"
                        "672195348"
                        "198342567"
                        "859761423"
                        "426853791"
                        "713924856"
                        "961537284"
                        "287419635"
                        "345286■79")
        self.assertTrue(sudoku.putNumber(1, 8, 6))
        over = sudoku.isOver()
        self.assertTrue(over)

    def test_win(self):
        sudoku = Sudoku("534678912"
                        "672195348"
                        "198342567"
                        "859761423"
                        "426853791"
                        "713924856"
                        "961537284"
                        "287419635"
                        "345286179")
        over = sudoku.isOver()
        self.assertTrue(over)

    def test_no_win(self):
        sudoku = Sudoku("53■■7■25■"
                        "■6■■195■■"
                        "■■98■■■■6"
                        "■8■■■6■■■"
                        "34■■8■3■■"
                        "17■■■2■■■"
                        "6■6■■■■28"
                        "■■■■419■■"
                        "5■■■■8■■7")
        over = sudoku.isOver()
        self.assertFalse(over)


if __name__ == '__main__':
    unittest.main()
