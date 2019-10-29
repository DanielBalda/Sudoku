from sudoku import (
    Sudoku,
    PositionFixed,
    NumberInRow,
    NumberInColumn,
    NumberInRegion
)
from api import (
    Api,
    ApiNotRespond
)
import os
from threading import Timer


class EmptyVar(Exception):
    pass


class InvalidNumber(Exception):
    pass


class InputChar(Exception):
    pass


class InputSymbol(Exception):
    pass


class Interface(object):

    def gameDifficult(self):
        #os.system("clear")
        self.boardSize = ''
        while self.boardSize != '4' and self.boardSize != '9':
            self.boardSize = input("Game Difficult? 4 or 9: ")
            os.system("clear")
        print("Chosen difficulty:", self.boardSize +
              "\n#### Game Starter! ####")
        try:
            self.api = Api(self.boardSize)
            self.sudoku = Sudoku(self.api.request())
        except ApiNotRespond:
            os.system("clear"), print("Ups! Something went wrong. Please retry again."), self.gameDifficult()

    def validateNumber(self, number, posx, posy):
        symbols = '[~!@#$%^&*()/_+{}":;\']+`.$'
        if set(symbols).intersection(number) or set(symbols).intersection(posx) or set(symbols).intersection(posy):
            raise InputSymbol()
        if number == "" or posx == "" or posy == "":
            raise EmptyVar()
        if number.isalpha() or posx.isalpha() or posy.isalpha():
            raise InputChar()
        if 0 < int(number) < 10 and -1 < int(posx) < int(self.boardSize) and -1 < int(posy) < int(self.boardSize):
            return True
        raise InvalidNumber()

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
            print("\n#### Game Over! ####")
        except PositionFixed:
            os.system("clear"), print("(!) This postion is fixed!"), self.game()

        except NumberInRow:
            os.system("clear"), print("(!) The number already exists in the Row!"), self.game()

        except NumberInColumn:
            os.system("clear"), print("(!) The number already exists in the Column!"), self.game()

        except NumberInRegion:
            os.system("clear"), print("(!) The number already exists in the Region!"), self.game()

        except InvalidNumber:
            os.system("clear"), print("(!) Only numbers between 1 and 9"), self.game()

        except InputChar:
            os.system("clear"), print("(!) Only numbers, not letters!"), self.game()

        except EmptyVar:
            os.system("clear"), print("(!) No spaces allowed"), self.game()

        except InputSymbol:
            os.system("clear"), print("(!) No symbol allowed"), self.game()

    def start(self):
        os.system("clear")
        self.gameDifficult()
        self.game()
