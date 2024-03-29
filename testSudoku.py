import unittest
from parameterized import parameterized
from sudoku import (
    Sudoku,
    PositionFixed,
    NumberInRow,
    NumberInColumn,
    NumberInRegion
)


class TestSudoku(unittest.TestCase):
    maxDiff = None

    # TABLERO 9x9
    @parameterized.expand([
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■17■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 3, 2, 4),
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■17■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 2, 0, 2),
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■17■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 8, 0, 8),
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■17■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 3, 8, 0),
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■17■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 5, 6, 2),
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■17■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 5, 4, 4)
    ])
    def test_put_numbers_9x9(self, board, number, x, y):
        sudoku = Sudoku(board)
        self.assertTrue(sudoku.putNumber(number, x, y))

    @parameterized.expand([
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■17■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 3, 8, 8),
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■17■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 5, 4, 3),
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■17■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 2, 0, 0),
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■17■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 6, 5, 8)
    ])
    def test_number_fixed_9x9(self, board, number, x, y):
        sudoku = Sudoku(board)
        with self.assertRaises(PositionFixed):
            sudoku.putNumber(number, x, y)

    @parameterized.expand([
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■17■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 5, 0, 5),
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■17■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 8, 2, 4),
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■17■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 7, 8, 0),
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■17■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 5, 7, 0)
    ])
    def test_number_exist_in_row_9x9(self, board, number, x, y):
        sudoku = Sudoku(board)
        with self.assertRaises(NumberInRow):
            sudoku.putNumber(number, x, y)

    @parameterized.expand([
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■17■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 9, 0, 5),
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■17■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 6, 0, 8),
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■17■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 5, 8, 0),
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■17■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 1, 8, 3)
    ])
    def test_number_exist_in_column_9x9(self, board, number, x, y):
        sudoku = Sudoku(board)
        with self.assertRaises(NumberInColumn):
            sudoku.putNumber(number, x, y)

    @parameterized.expand([
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■17■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 9, 0, 2),
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■17■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 6, 0, 6),
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■17■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 2, 7, 7),
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■17■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 4, 3, 2)
    ])
    def test_number_exist_in_region_9x9(self, board, number, x, y):
        sudoku = Sudoku(board)
        with self.assertRaises(NumberInRegion):
            sudoku.putNumber(number, x, y)

    @parameterized.expand([
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■■7■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 8, 0, 8, 2),
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■■7■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 2, 0, 8, 8),
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■■7■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 4, 0, 8, 1),
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■■7■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79", 1, 0, 8, 4)
    ])
    def test_number_over_number_not_fixed_9x9(self, board, number, x, y, number2):
        sudoku = Sudoku(board)
        self.assertTrue(sudoku.putNumber(number, x, y))
        self.assertTrue(sudoku.putNumber(number2, x, y))

    @parameterized.expand([
        ("53■■7■■■■6■■195■■■■98■■■■6■8■■■6■■■34■■8■3■■17■■■2■■■6■6■■■■28■"
         "■■■419■■5■■■■8■■79"),
        ("■3■■4■■2■■9■27■3■■■■■5■38■■■2■8■74■■68■■3■■9■■5■■■6■■■■■4■6■9■■"
         "■13■■■6■■2■53■■1■8"),
        ("■■■■■35■■■5■■2■3■■■6■■4■■7263587■■■■■72■6■■■■■■■235■■432■■■■■■8"
         "596■■■■■■8■4■■■■53")
    ])
    def test_game_not_over_9x9(self, board):
        sudoku = Sudoku(board)
        self.assertFalse(sudoku.isOver())

    def test_game_not_over_2_9x9(self):
        sudoku = Sudoku("53■■7■■■■6■■195■■2■98■■■■6■8■■■6■■■34■■8■3■■1"
                        "7■■■2■■■6■6■3■■28■■■■419■■5■■■■8■■79")
        self.assertTrue(sudoku.putNumber(4, 2, 4))
        self.assertTrue(sudoku.putNumber(5, 3, 6))
        self.assertTrue(sudoku.putNumber(3, 2, 4))
        self.assertFalse(sudoku.isOver())

    @parameterized.expand([
        ("534678912672195348198342567859766423426853791"
         "71392485696153728428748963345286■793", 1, 8, 5),
        ("938564721416372895527198463754629318169483257"
         "2837516496718■5932895236174342917586", 4, 6, 4),
        ("2596■7184683412579147859236416395827578241963"
         "932768451864923715795186342321574698", 3, 0, 4)
    ])
    def test_win_after_last_play_9x9(self, board, number, x, y):
        sudoku = Sudoku(board)
        self.assertTrue(sudoku.putNumber(number, x, y))
        self.assertTrue(sudoku.isOver())

    @parameterized.expand([
        ("534678912672195348198342567859761423426853791"
         "713924856961537284287419635345286179"),
        ("98354617254271986376182345935468129729837461"
         "5617295348179432586425968731836157924"),
        ("86529147327146398594378561231685429745967283"
         "1782319546628937154197546328534128769")
    ])
    def test_win_9x9(self, board):
        sudoku = Sudoku(board)
        self.assertTrue(sudoku.isOver())

    @parameterized.expand([
        ("53■67891267■■953481983■■■6785976142■■26853■91"
         "713924856961537284287419635345286179"),
        ("983546172542719863■6182345935468129729837461"
         "56172953481794325864259687■1836157924"),
        ("86529147327146398594378561231685429745967283"
         "17823195466289■7154197546328534128769")
    ])
    def test_no_win_9x9(self, board):
        sudoku = Sudoku(board)
        self.assertFalse(sudoku.isOver())

    # TABLERO 4x4

    @parameterized.expand([
        ("1■3■5678■12345■7", 7, 0, 1),
        ("1■3■5678■12345■7", 5, 0, 3),
        ("1■3■5678■12345■7", 8, 2, 0),
        ("1■3■5678■12345■7", 6, 3, 2),
        ("■43■23■44■■■32■■", 5, 0, 0),
        ("■43■23■44■■■32■■", 7, 3, 3)
    ])
    def test_put_numbers_4x4(self, board, number, x, y):
        sudoku = Sudoku(board)
        self.assertTrue(sudoku.putNumber(number, x, y))

    @parameterized.expand([
        ("1■3■5678■12345■7", 3, 0, 0),
        ("1■3■5678■12345■7", 8, 3, 3),
        ("■43■23■44■■■32■■", 9, 0, 2),
        ("■43■23■44■■■32■■", 4, 3, 1)
    ])
    def test_number_fixed_4x4(self, board, number, x, y):
        sudoku = Sudoku(board)
        with self.assertRaises(PositionFixed):
            sudoku.putNumber(number, x, y)

    @parameterized.expand([
        ("1■3■5678■12345■7", 5, 3, 2),
        ("1■3■5678■12345■7", 1, 0, 3),
        ("■43■23■44■■■32■■", 3, 0, 0),
        ("■43■23■44■■■32■■", 4, 2, 3)
    ])
    def test_number_exist_in_row_4x4(self, board, number, x, y):
        sudoku = Sudoku(board)
        with self.assertRaises(NumberInRow):
            sudoku.putNumber(number, x, y)

    @parameterized.expand([
        ("1■3■5678■12345■7", 6, 0, 1),
        ("1■3■5678■12345■7", 2, 3, 2),
        ("■43■23■44■■■32■■", 3, 2, 2),
        ("■43■23■44■■■32■■", 3, 2, 1)
    ])
    def test_number_exist_in_column_4x4(self, board, number, x, y):
        sudoku = Sudoku(board)
        with self.assertRaises(NumberInColumn):
            sudoku.putNumber(number, x, y)

    @parameterized.expand([
        ("1■3■5678■12347■7", 5, 0, 1),
        ("1■3■5668■12745■3", 7, 3, 2),
        ("■43■25■44■■■32■■", 5, 0, 0),
        ("■43■23■44■■■32■5", 5, 2, 2)
    ])
    def test_number_exist_in_region_4x4(self, board, number, x, y):
        sudoku = Sudoku(board)
        with self.assertRaises(NumberInRegion):
            sudoku.putNumber(number, x, y)

    @parameterized.expand([
        ("1■3■5678■12347■7", 2, 0, 1, 8),
        ("1■3■5668■12745■3", 8, 3, 2, 9),
        ("■43■25■44■■■32■■", 6, 0, 0, 1),
        ("■43■23■44■■■32■5", 8, 3, 2, 6)
    ])
    def test_number_over_number_not_fixed_4x4(self, board, number, x, y, number2):
        sudoku = Sudoku(board)
        self.assertTrue(sudoku.putNumber(number, x, y))
        self.assertTrue(sudoku.putNumber(number2, x, y))

    @parameterized.expand([
        ("1■3■5678■12347■7"),
        ("1■3■5668■12745■3"),
        ("■43■25■44■■■32■■"),
        ("■43■23■44■■■32■5")
    ])
    def test_game_not_over_4x4(self, board):
        sudoku = Sudoku(board)
        self.assertFalse(sudoku.isOver())

    def test_game_not_over_2_4x4(self):
        sudoku = Sudoku("■43■23■44■■■32■5")
        self.assertTrue(sudoku.putNumber(5, 0, 0))
        self.assertTrue(sudoku.putNumber(7, 0, 3))
        self.assertTrue(sudoku.putNumber(1, 0, 0))
        self.assertFalse(sudoku.isOver())

    @parameterized.expand([
        ("1342423■31242413", 1, 1, 3),
        ("134224313124421■", 3, 3, 3),
        ("1■23231442313142", 4, 0, 1)
    ])
    def test_win_after_last_play_4x4(self, board, number, x, y):
        sudoku = Sudoku(board)
        self.assertTrue(sudoku.putNumber(number, x, y))
        self.assertTrue(sudoku.isOver())

    @parameterized.expand([
        ("4231132424133142"),
        ("3412123441232341"),
        ("4132234114233214")
    ])
    def test_win_4x4(self, board):
        sudoku = Sudoku(board)
        self.assertTrue(sudoku.isOver())

    @parameterized.expand([
        ("4■31132424133142"),
        ("3412123■41232341"),
        ("41322341142332■4")
    ])
    def test_no_win_4x4(self, board):
        sudoku = Sudoku(board)
        self.assertFalse(sudoku.isOver())

    # DIBUJADO DEL TABLERO

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
                                             "-------------------------------------")

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
                                             "-----------------")


if __name__ == '__main__':
    unittest.main()
