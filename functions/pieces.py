whiteCoords = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

blackCoords = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

whiteStarting = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

blackStarting = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

whiteSetup = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook", 
              "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]

blackSetup = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook", 
              "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]


turn = 0 # reset to 0 on new game
selection = 123 # random value, indicates there is no selected piece
selected = False
validmoves = []
tar_pos = 0

class Pawn():
    def __init__(self):
        pass

class Rook():
    def __init__(self):
        pass

class Bishop():
    def __init__(self):
        pass

class Knight():
    def __init__(self):
        pass

class Queen():
    def __init__(self):
        pass

class King():
    def __init__(self):
        pass