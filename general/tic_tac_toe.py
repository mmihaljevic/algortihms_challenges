"""
How would you determine if someone has won a game of tic-tac-toe on a board of any size?

For someone to won a tic-tac-toe - needs to have row, column or diagonal (left-right) set 
to same elements

Board is represented by 2D array:
0 - empty
1 - player one
2 - player two
e.q:
[[1, 2, 1], [1, 1, 1], [0, 2, 2]] - player one won the game

"""

class TicTacToe(object):

    def __init__(self, board_len, board):
        ''' initialize the game with board_len and board '''
        self.board_len = board_len
        self.board = board 

    def __str__(self):
        ''' nice output '''
        res = []
        for row in self.board:
            res.append(str(row))
 
        return '\n'.join(res)

    def check(self, path):
        check = reduce(lambda x, y: x & y, path)
        if check in [1, 2]:
            return "".join(["Player: " ,str(check), " won!"]) 
        return False

    def someone_won(self):
        ''' has someone won the game '''
        # check rows
        for row in self.board:
            check = self.check(row)
            if check:
                return check          
        # check columns
        for i in xrange(self.board_len):
            column = [self.board[x][i] for x in xrange(self.board_len)]
            check = self.check(column)
            if check:
                return check           

        # check left diag
        left_diag = [self.board[i][i] for i in xrange(self.board_len)]
        check = self.check(left_diag)
        if check:
            return check

        # check right diag
        right_diag = [self.board[i][self.board_len -1 -i] for i in xrange(self.board_len)]
        check = self.check(right_diag)
        if check:
            return check 
        return "No one won !"



# test cases
# noone won 3x3 
board1 = [[1, 2, 1], [2, 1, 2], [1, 2, 2]]

t = TicTacToe(3, board1)
print t
print t.someone_won()         
