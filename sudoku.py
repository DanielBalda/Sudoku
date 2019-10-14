class Sudoku(object):
    def __init__(self, board):
        self.board = [[board[i+j*9] for i in range(9)] for j in range(9)]
        self.copyBoard = self.board

    def numberInRow(self, number, posx):
        return str(number) in self.board[posx]

    def numberInColumn(self, number, posy):
        for x in range(9):
            if str(number) == self.board[x][posy]:
                return True
        return False

    # Falta Terminar
    def numberInRegion(self, number, posx, posy):
        pass

    # Como manejar Exepciones?
    def putNumber(self, number, posx, posy):
        if self.copyBoard[posx][posy] != 'X':
            return False
        elif self.numberInRow(number, posx):
            return False
        elif self.numberInColumn(number, posy):
            return False
        elif self.numberInRegion(number, posx, posy):
            return False
        self.board[posx][posy] = str(number)
        return True

    def isOver(self):
        return 'X' not in self.board[0]
