import pygame

from functions.pieces import *
from functions.const import *
from functions.assets import *

def drawBoard():
    for i in range(64):
        row = i // 8
        column = i % 8
        if (row % 2 == 0 and column % 2 == 0) or (row % 2 != 0 and column % 2 != 0):
            pygame.draw.rect(WIN, Color2, [column * blockSize, row * blockSize, blockSize, blockSize])
        else:
            pygame.draw.rect(WIN, Color1, [column * blockSize, row * blockSize, blockSize, blockSize])

def drawPieces():
    # draw black
    for i in range(16):
        x = i * blockSize
        ymain = 0
        ypawn = blockSize
        if blackSetup[i] != "pawn":
            WIN.blit(blackAssets[i], (x, ymain))
        WIN.blit(blackAssets[8], (x, ypawn))

    # draw white
    for i in range(16):
        x = i * blockSize
        ymain = blockSize * 7
        ypawn = blockSize * 6
        if whiteSetup[i] != "pawn":
            WIN.blit(whiteAssets[i], (x, ymain))
        WIN.blit(whiteAssets[8], (x, ypawn))

def uptBoard():
    # draw black
    index = -1
    for i in blackCoords:
        x = i[0] * blockSize
        y = i[1] * blockSize
        index += 1
        if blackSetup[index] != "pawn":
            WIN.blit(blackAssets[index], (x, y))
            continue
        WIN.blit(blackAssets[8], (x, y))
    # draw white
    index = -1
    for i in whiteCoords:
        x = i[0] * blockSize
        y = i[1] * blockSize
        index += 1
        if whiteSetup[index] != "pawn":
            WIN.blit(whiteAssets[index], (x, y))
            continue
        WIN.blit(whiteAssets[8], (x, y))
    return True

def drawPossible(possibleMoves):
    for i in possibleMoves:
        x = i[0]
        y = i[1]
        if (x % 2 == 0 and y % 2 == 0) or (x % 2 != 0 and y % 2 != 0):
            pygame.draw.rect(WIN, Color2sel, [x * blockSize, y * blockSize, blockSize, blockSize])
        else:
            pygame.draw.rect(WIN, Color1sel, [x * blockSize, y * blockSize, blockSize, blockSize])
    uptBoard()

for event in pygame.event.get():
    if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
        print("hi")
        themecol1 = (118, 150, 86)
        themecol2 = (238, 238, 210)
        if Color1[1] != themecol1[1]:
            Color1 = (118, 150, 86)
        elif Color1[1] == themecol1[1]:
            Color1 = (195, 160, 130)

        if Color2[1] != themecol2[1]:
            Color2 = (238, 238, 210)
        elif Color2[1] == themecol2[1]:
            Color2 = (242, 225, 195)
        drawBoard()