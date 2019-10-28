import unittest
from sudoku import (
    Sudoku,
    PositionFixed,
    NumberInRow,
    NumberInColumn,
    NumberInRegion
)


class TestSudoku(unittest.TestCase):
    maxDiff = None

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

    def test_number_fixed(self):
        sudoku = Sudoku("53■■7■■■■"
                        "6■■195■■2"
                        "■98■■■■6■"
                        "8■■■6■■■3"
                        "4■■8■3■■1"
                        "7■■■2■■■6"
                        "■6■3■■28■"
                        "■■■419■■5"
                        "■■■■8■■79")
        with self.assertRaises(PositionFixed):
            sudoku.putNumber(1, 5, 8)

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
        with self.assertRaises(NumberInRow):
            sudoku.putNumber(5, 0, 7)

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
        with self.assertRaises(NumberInColumn):
            sudoku.putNumber(9, 0, 8)

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
        with self.assertRaises(NumberInRegion):
            sudoku.putNumber(7, 6, 6)

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

    def test_number_over_number_not_fixed(self):
        sudoku = Sudoku("53■■7■■■■"
                        "6■■195■■2"
                        "■98■■■■6■"
                        "8■■■6■■■3"
                        "4■■8■3■■1"
                        "7■■■2■■■6"
                        "■6■3■■28■"
                        "■■■419■■5"
                        "■■■■8■■75")
        self.assertTrue(sudoku.putNumber(9, 8, 0))
        self.assertTrue(sudoku.putNumber(3, 8, 0))

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
        self.assertTrue(sudoku.putNumber(4, 2, 4))
        self.assertTrue(sudoku.putNumber(5, 3, 6))
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

    def test_win_4x4(self):
        sudoku = Sudoku("4231"
                        "1342"
                        "3124"
                        "2413")
        over = sudoku.isOver()
        self.assertTrue(over)

    def test_no_win_4x4(self):
        sudoku = Sudoku("423■"
                        "1342"
                        "■12■"
                        "2■13")
        over = sudoku.isOver()
        self.assertFalse(over)

    def test_board_print_9x9(self):
        sudoku = Sudoku("53■■7■25■"
                        "■6■■195■■"
                        "■■98■■■■6"
                        "■8■■■6■■■"
                        "34■■8■3■■"
                        "17■■■2■■■"
                        "6■6■■■■28"
                        "■■■■419■■"
                        "5■■■■8■■7")
        self.assertEqual(sudoku.printBoard(),"-------------------------------------\n"
                                             "| 5   3   ■ | ■   7   ■ | 2   5   ■ |\n"
                                             "|   -   -   -   -   -   -   -   -   |\n"
                                             "| ■   6   ■ | ■   1   9 | 5   ■   ■ |\n"
                                             "|   -   -   -   -   -   -   -   -   |\n"
                                             "| ■   ■   9 | 8   ■   ■ | ■   ■   6 |\n"
                                             "|---+---+---+---+---+---+---+---+---|\n"
                                             "| ■   8   ■ | ■   ■   6 | ■   ■   ■ |\n"
                                             "|   -   -   -   -   -   -   -   -   |\n"
                                             "| 3   4   ■ | ■   8   ■ | 3   ■   ■ |\n"
                                             "|   -   -   -   -   -   -   -   -   |\n"
                                             "| 1   7   ■ | ■   ■   2 | ■   ■   ■ |\n"
                                             "|---+---+---+---+---+---+---+---+---|\n"
                                             "| 6   ■   6 | ■   ■   ■ | ■   2   8 |\n"
                                             "|   -   -   -   -   -   -   -   -   |\n"
                                             "| ■   ■   ■ | ■   4   1 | 9   ■   ■ |\n"
                                             "|   -   -   -   -   -   -   -   -   |\n"
                                             "| 5   ■   ■ | ■   ■   8 | ■   ■   7 |\n"
                                             "-------------------------------------\n")

    def test_board_print_4x4(self):
        sudoku = Sudoku("1■3■"
                        "5678"
                        "■123"
                        "45■7")
        self.assertEqual(sudoku.printBoard(),"-----------------\n"
                                             "| 1   ■ | 3   ■ |\n"
                                             "|   -   -   -   |\n"
                                             "| 5   6 | 7   8 |\n"
                                             "|   -   -   -   |\n"
                                             "| ■   1 | 2   3 |\n"
                                             "|   -   -   -   |\n"
                                             "| 4   5 | ■   7 |\n"
                                             "-----------------\n")


if __name__ == '__main__':
    unittest.main()
