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
        self.boardSize = ''
        while self.boardSize != '4' and self.boardSize != '9':
            self.boardSize = input("\u001b[34;1mGame Difficult? 4 or 9:\033[0m ")
            os.system("clear")
        print("\u001b[34;1mChosen difficulty:", self.boardSize +
              "\n#### Game Starter! ####\033[0m")
        try:
            self.api = Api(self.boardSize)
            self.sudoku = Sudoku(self.api.request())
        except ApiNotRespond:
            os.system("clear"), print("\033[91mUps! Something went wrong. Please retry again.\033[0m"), self.gameDifficult()

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
                self.number = input("\n\033[94m#\033[0m Place number: ")
                self.posx = input("\033[94m#\033[0m Place position in X: ")
                self.posy = input("\033[94m#\033[0m Place position in Y: ")
                if self.validateNumber(self.number, self.posx, self.posy):
                    self.sudoku.putNumber(int(self.number), int(self.posx), int(self.posy))
                    os.system("clear")
                    print(self.sudoku.printBoard())
            print("\n\033[92m#### Game Over! ####\033[0m")
        except PositionFixed:
            os.system("clear"), print("\033[91m(!)\033[0m This postion is fixed!")

        except NumberInRow:
            os.system("clear"), print("\033[91m(!)\033[0m The number already exists in the Row!")

        except NumberInColumn:
            os.system("clear"), print("\033[91m(!)\033[0m The number already exists in the Column!")

        except NumberInRegion:
            os.system("clear"), print("\033[91m(!)\033[0m The number already exists in the Region!")

        except InvalidNumber:
            os.system("clear"), print("\033[91m(!)\033[0m Only numbers between 1 and 9.\n    X & Y between 0 and " + str(int(self.boardSize)-1) + ".")

        except InputChar:
            os.system("clear"), print("\033[91m(!)\033[0m Only numbers, not letters!")

        except EmptyVar:
            os.system("clear"), print("\033[91m(!)\033[0m No spaces allowed")

        except InputSymbol:
            os.system("clear"), print("\033[91m(!)\033[0m No symbol allowed")
        self.game()

    def start(self):
        os.system("clear")
        self.gameDifficult()
        self.game()
