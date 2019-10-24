import copy


class PositionFixed(Exception):
    pass


class NumberInRow(Exception):
    pass


class NumberInColumn(Exception):
    pass


class NumberInRegion(Exception):
    pass


class Sudoku(object):
    def __init__(self, board):
        self.size = int(len(board)**.5)
        self.board = [[board[i+j*self.size] for i in range(self.size)] for j in range(self.size)]
        self.copyBoard = copy.deepcopy(self.board)

    def numberInRow(self, number, posx):
        return str(number) in self.board[posx]

    def numberInColumn(self, number, posy):
        for x in range(self.size):
            if str(number) == self.board[x][posy]:
                return True

    def numberInRegion(self, number, posx, posy):
        aux = int(self.size**.5)
        difPosx = posx // aux
        difPosy = posy // aux
        for row in range(aux):
            for column in range(aux):
                if self.board[difPosx*aux+row][difPosy*aux+column] \
                     == str(number):
                    return True

    def putNumber(self, number, posx, posy):
        if self.copyBoard[posx][posy] != '■':
            raise PositionFixed()
        elif self.numberInRow(number, posx):
            raise NumberInRow()
        elif self.numberInColumn(number, posy):
            raise NumberInColumn()
        elif self.numberInRegion(number, posx, posy):
            raise NumberInRegion()
        self.board[posx][posy] = str(number)
        return True

    def printBoard(self):
        printing = ''
        if len(self.board) == 9:
            elements = " {}   {}   {} |"
            lines = 37
        else:
            elements = " {}   {} |"
            lines = 17
        printing += "-"*lines + "\n"
        for i, row in enumerate(self.board):
            printing += (("|" + elements * int(len(self.board)**.5)).format(*[x if x != 0 else " " for x in row])) + "\n"
            if i == (len(self.board)-1):
                printing += ("-"*lines) + "\n"
            elif i % (len(self.board)**.5) == 2:
                printing += ("|" + "---+"*(len(self.board)-1) + "---|") + "\n"
            else:
                printing += ("|" + "   -"*(len(self.board)-1) + "   |") + "\n"
        return printing

    def isOver(self):
        for i in range(int(self.size)):
            if '■' in self.board[i]:
                return False
        return True
