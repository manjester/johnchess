import pygame

from functions.const import *
from functions.pieces import *
from functions.assets import *
from functions.draw import *
from functions.moves import *
from functions.text import *

possibleMoves = []

drawBoard()
drawPieces()
blackOptions = check_options(blackSetup, blackCoords, 'black')
whiteOptions = check_options(whiteSetup, whiteCoords, 'white')

run = True
gameend = False
floatingtext()
while run:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False

        if turn % 2 == 0:
            if not gameend:
                pygame.display.set_caption("Casual Chess: White to play")
            else:
                pygame.display.set_caption("Casual Chess: GAME OVER. Black wins!")
                endscreen("black")
        elif turn % 2 == 1:
            if not gameend:
                pygame.display.set_caption("Casual Chess: Black to play")
            else:
                pygame.display.set_caption("Casual Chess: GAME OVER. White wins!")
                endscreen("white")

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            if gameend:
                pygame.display.set_caption("Casual Chess: White to play")
                gameend = False
            for i in range(16):
                blackCoords[i] = blackStarting[i]
                whiteCoords[i] = whiteStarting[i]
            drawBoard()
            uptBoard()
            floatingtext()
            turn = 0

        if not gameend:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                cursor_x = event.pos[0] // blockSize
                cursor_y = event.pos[1] // blockSize
                cursorPos = (cursor_x, cursor_y)

                if turn % 2 == 0: # white turn
                    validmoves = check_valid_moves()

                    if cursorPos in whiteCoords:
                        drawBoard()
                        selection = whiteCoords.index(cursorPos)
                        possibleMoves = possible(selection, "white")
                        drawPossible(possibleMoves)

                    if cursorPos in possibleMoves and selection != 123:
                        whiteCoords[selection] = cursorPos

                        if cursorPos in blackCoords:
                            black_piece = blackCoords.index(cursorPos)
                            blackCoords[black_piece] = (100, 100)

                            if black_piece == 4:
                                gameend = True
                        drawBoard()
                        uptBoard()
                        blackOptions = check_options(blackSetup, blackCoords, 'black')
                        whiteOptions = check_options(whiteSetup, whiteCoords, 'white')
                        black_piece = 0
                        black_index = 0
                        possibleMoves = []
                        turn += 1
                        selection = 123
                        validmoves = []

                if turn % 2 == 1: # black turn
                    validmoves = check_valid_moves()

                    if cursorPos in blackCoords:
                        drawBoard()
                        selection = blackCoords.index(cursorPos)
                        possibleMoves = possible(selection, "black")
                        drawPossible(possibleMoves)

                    if cursorPos in possibleMoves and selection != 123:
                        blackCoords[selection] = cursorPos

                        if cursorPos in whiteCoords:
                            white_piece = whiteCoords.index(cursorPos)
                            whiteCoords[white_piece] = (100, 100)

                            if white_piece == 4:
                                gameend = True
                        drawBoard()
                        uptBoard()
                        blackOptions = check_options(blackSetup, blackCoords, 'black')
                        whiteOptions = check_options(whiteSetup, whiteCoords, 'white')
                        white_piece = 0
                        possibleMoves = []
                        turn += 1
                        selection = 123
                        validmoves = []
            
    pygame.display.update()
pygame.quit()