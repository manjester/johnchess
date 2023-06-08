import pygame

from functions.const import *

pieceSize = (blockSize, blockSize)

"""Assign texture for the pieces"""
# black
black_queen = pygame.image.load('assets/images/QueenB.png')
black_queen = pygame.transform.scale(black_queen, pieceSize)
black_bishop = pygame.image.load('assets/images/BishopB.png')
black_bishop = pygame.transform.scale(black_bishop, (blockSize, blockSize))
black_knight = pygame.image.load('assets/images/KnightB.png')
black_knight = pygame.transform.scale(black_knight, pieceSize)
black_rook = pygame.image.load('assets/images/RookB.png')
black_rook = pygame.transform.scale(black_rook, pieceSize)
black_king = pygame.image.load('assets/images/KingB.png')
black_king = pygame.transform.scale(black_king, pieceSize)
black_pawn = pygame.image.load('assets/images/PawnB.png')
black_pawn = pygame.transform.scale(black_pawn, pieceSize)
# white
white_queen = pygame.image.load('assets/images/QueenW.png')
white_queen = pygame.transform.scale(white_queen, pieceSize)
white_bishop = pygame.image.load('assets/images/BishopW.png')
white_bishop = pygame.transform.scale(white_bishop, pieceSize)
white_knight = pygame.image.load('assets/images/KnightW.png')
white_knight = pygame.transform.scale(white_knight, pieceSize)
white_rook = pygame.image.load('assets/images/RookW.png')
white_rook = pygame.transform.scale(white_rook, pieceSize)
white_king = pygame.image.load('assets/images/KingW.png')
white_king = pygame.transform.scale(white_king, pieceSize)
white_pawn = pygame.image.load('assets/images/PawnW.png')
white_pawn = pygame.transform.scale(white_pawn, pieceSize)

# index for drawing pieces
whiteSetup = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
blackSetup = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]

whiteAssets = [white_rook, white_knight, white_bishop, white_queen, white_king, white_bishop, white_knight, white_rook, white_pawn]
blackAssets = [black_rook, black_knight, black_bishop, black_queen, black_king, black_bishop, black_knight, black_rook, black_pawn]