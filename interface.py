from sudoku import Sudoku
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
            return 0 < int(self.number) < 10 and \
              -1 < int(self.posx) < int(self.boardSize) and \
              -1 < int(self.posy) < int(self.boardSize)
        except Exception:
            return False

    def play(self):
        self.gameDifficult()
        print(self.sudoku.printBoard())
        while not self.sudoku.isOver():
            self.number = input("\nPlace number: ")
            self.posx = input("Place position in X: ")
            self.posy = input("Place position in Y: ")
            if self.validateNumber(self.number, self.posx, self.posy):
                self.sudoku.putNumber(int(self.number), int(self.posx), int(self.posy))
                os.system("clear")
                self.sudoku.printBoard()
            else:
                os.system("clear")
                print("Invalid!!!. Place other number.")
                self.sudoku.printBoard()
        print("\n#### Game Over! ####")


sudokuGame = Interface()
sudokuGame.play()

#tablero 4x4 resuelto = "4231132421433412"
#tablero 9x9 resuelto = "682341579147956823593287146256479318319628754478135962865792431924513687731864295"