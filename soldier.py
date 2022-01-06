class Soldier():
    def __init__(self, kind, side, turn = 0):
        self.kind = kind
        self.side = side
        self.turn = turn

class Board():
    def __init__(self):
        self.board = []
        board_setup = open('assets/setup.txt').read()
        for row in board_setup.split('\n'):
            board_row = []
            for soldier in row.split(','):
                board_row.append(Soldier(soldier[0], soldier[1]))
            self.board.append(board_row)
    