import pygame

from functions.const import *
from functions.pieces import *
from functions.assets import *
from functions.draw import *

def pawnmove(position, color):
    if color == "white":
        moves = [(position[0], position[1] - 1), (position[0], position[1] - 2)]
        for i in blackCoords:
            dx = i[0]
            dy = i[1]
            if (position[0], position[1] - 2) in moves:
                if position[1] == 6 and dx == position[0] and position[1] - 2 == dy:
                    moves.remove((position[0], position[1] - 2))
                if position[1] != 6:
                    moves.remove((position[0], position[1] - 2))
            if dx == position[0] and dy == position[1] - 1:
                moves.remove((position[0], position[1] - 1))
            if dx == position[0] + 1 and dy == position[1] - 1:
                moves.append((position[0] + 1, position[1] - 1))
            if dx == position[0] - 1 and dy == position[1] - 1:
                moves.append((position[0] - 1, position[1] - 1))
        return moves
    else:
        moves = [(position[0], position[1] + 1), (position[0], position[1] + 2)]
        for i in whiteCoords:
            dx = i[0]
            dy = i[1]
            if (position[0], position[1] + 2) in moves:
                if position[1] == 1 and dx == position[0] and position[1] + 2 == dy:
                    moves.remove((position[0], position[1] + 2))
                if position[1] != 1:
                    moves.remove((position[0], position[1] + 2))
            if dx == position[0] and dy == position[1] + 1:
                moves.remove((position[0], position[1] + 1))
            if dx == position[0] + 1 and dy == position[1] + 1:
                moves.append((position[0] + 1, position[1] + 1))
            if dx == position[0] - 1 and dy == position[1] + 1:
                moves.append((position[0] - 1, position[1] + 1))
        return moves

def knightmove(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = blackCoords
        friends_list = whiteCoords
    else:
        friends_list = blackCoords
        enemies_list = whiteCoords
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

def rookmove(position, color):
    moves = []
    if color == 'white':
        enemies_list = blackCoords
        friends_list = whiteCoords
    else:
        friends_list = blackCoords
        enemies_list = whiteCoords
    for i in range(4):  # down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves

def kingmove(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = blackCoords
        friends_list = whiteCoords
    else:
        friends_list = blackCoords
        enemies_list = whiteCoords
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

def kingcheck(locator, turn):
    moves = []
    checked = []
    if turn == "white":
        for i in kingmove(locator, turn):
            if i not in blackOptions:
                moves.append(i)
        if locator in blackOptions:
            checked.append(locator)
    if turn == "black":
        for i in kingmove(locator, turn):
            if i not in whiteOptions:
                moves.append(i)
        if locator in whiteOptions:
            checked.append(locator)

    for i in moves:
        if i in checked:
            moves.remove(i)

    return moves, checked

def blockcheck(locator, turn):
    right, left, below, above = 0
    new = [24, 3]
    attacking = []
    kingmoves = kingcheck(locator, turn)
    if kingmoves[1]:
        if turn == "white":
            options = check_options(blackSetup, blackCoords, "black")
            for i in range(16):
                atk = possible(i, "black")
                if locator in atk:
                    if blackSetup[i] == "bishop":
                        pos = blackCoords[i]
                        for j in range(8):
                            if (locator[0] == 8 or locator[0] == 8 or locator[0] < 0 or locator[0] < 0) and new != [24, 3]:
                                break
                            if locator[0] < pos[0]:
                                right = 1
                            else:
                                left = 1
                            if locator[1] < pos[1]:
                                below = 1
                            else:
                                above = 1
                            if right:
                                new[0] = locator[0] + j
                                if below:
                                    new[1] = locator[1] + j
                                elif above:
                                    locator[1] - j
                            elif left:
                                new[0] = locator[0] - j
                                if below:
                                    new[1] = locator[1] + j
                                elif above:
                                    new[1] = locator[1] - j
                            attacking.append(new)
        else:
            options = check_options(whiteSetup, whiteCoords, "white")

        

def queenmove(position, color):
    moves_list = bishopmove(position, color)
    second_list = rookmove(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list

def bishopmove(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = blackCoords
        friends_list = whiteCoords
    else:
        friends_list = blackCoords
        enemies_list = whiteCoords
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

def possible(index, turn):
    moves = []
    if turn == "white":
        locator = whiteCoords[index]
        kingmoves = kingcheck(whiteCoords[4], turn)
    else:
        locator = blackCoords[index]
        kingmoves = kingcheck(blackCoords[4], turn)
    
    if whiteSetup[index] == "king" or blackSetup[index] == "king":
        for i in kingmoves[0]:
            moves.append(i)
    """ if kingmoves[1]: # if king is in check, then only possible moves are king moves
        return moves """
        
    if whiteSetup[index] == "pawn" or blackSetup[index] == "pawn":
        for i in pawnmove(locator, turn):
            moves.append(i)
    if whiteSetup[index] == "rook" or blackSetup[index] == "rook":
        for i in rookmove(locator, turn):
            moves.append(i)
    if whiteSetup[index] == "bishop" or blackSetup[index] == "bishop":
        for i in bishopmove(locator, turn):
            moves.append(i)
    if whiteSetup[index] == "knight" or blackSetup[index] == "knight":
        for i in knightmove(locator, turn):
            moves.append(i)
    if whiteSetup[index] == "queen" or blackSetup[index] == "queen":
        for i in queenmove(locator, turn):
            moves.append(i)
    return moves
    
def check_options(setups, coords, turn):
    moves = []
    for i in range(len(coords)):
        locator = coords[i]
        piece = setups[i]
        if piece == "pawn":
            for i in pawnmove(locator, turn):
                moves.append(i)
        if piece == "rook":
            for i in rookmove(locator, turn):
                moves.append(i)
        if piece == "bishop":
            for i in bishopmove(locator, turn):
                moves.append(i)
        if piece == "knight":
            for i in knightmove(locator, turn):
                moves.append(i)
        if piece == "queen":
            for i in queenmove(locator, turn):
                moves.append(i)
        if piece == "king":
            for i in kingmove(locator, turn):
                moves.append(i)
    return moves

blackOptions = check_options(blackSetup, blackCoords, "black")
whiteOptions = check_options(whiteSetup, whiteCoords, "white")

def check_valid_moves():
    if turn % 2 == 0:
        options = whiteOptions
    else:
        options = blackOptions
    return options