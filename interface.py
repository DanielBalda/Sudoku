from sudoku import (
    Sudoku,
    PositionFixed,
    NumberInRow,
    NumberInColumn,
    NumberInRegion
)
from api import Api
import os


class Interface(object):

    def gameDifficult(self):
        os.system("clear")
        self.boardSize = ''
        while self.boardSize != '4' and self.boardSize != '9':
            self.boardSize = input("Game Difficult? 4 or 9: ")
            os.system("clear")
        print("Chosen difficulty:", self.boardSize +
              "\n#### Game Starter! ####")
        self.api = Api(self.boardSize)
        self.sudoku = Sudoku(self.api.request())

    def validateNumber(self, number, posx, posy):
        try:
            if 0 < int(number) < 10 and -1 < int(posx) < int(self.boardSize) and -1 < int(posy) < int(self.boardSize):
                return True
        except Exception:
            return False

    def game(self):
        print(self.sudoku.printBoard())
        try:
            while not self.sudoku.isOver():
                self.number = input("\nPlace number: ")
                self.posx = input("Place position in X: ")
                self.posy = input("Place position in Y: ")
                if self.validateNumber(self.number, self.posx, self.posy):
                    self.sudoku.putNumber(int(self.number), int(self.posx), int(self.posy))
                    os.system("clear")
                    print(self.sudoku.printBoard())
                else:
                    os.system("clear")
                    print("Place valid numbers.")
                    print(self.sudoku.printBoard())
            print("\n#### Game Over! ####")
        except PositionFixed:
            os.system("clear"), print("This postion is fixed!"), self.game()

        except NumberInRow:
            os.system("clear"), print("The number already exists in the Row!"), self.game()

        except NumberInColumn:
            os.system("clear"), print("The number already exists in the Column!"), self.game()

        except NumberInRegion:
            os.system("clear"), print("The number already exists in the Region!"), self.game()

    def start(self):
        self.gameDifficult()
        self.game()
