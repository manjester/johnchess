import pygame

from functions.const import *

textCol1 = (0, 0, 0)
textCol2 = (255, 255, 255)

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 32)
font2 = pygame.font.SysFont('Comic Sans MS', 32)
text = font.render("Press 'R' to restart!", True, textCol1)
outline = font2.render("Press 'R' to restart!", True, textCol2)
text2 = font.render("Black wins!", True, textCol1)
outline2 = font2.render("Black wins!", True, textCol2)
text3 = font.render("White wins!", True, textCol1)
outline3 = font2.render("White wins!", True, textCol2)

def floatingtext():
    WIN.blit(outline, (1/3 * blockSize - int(1/30 * blockSize), HEIGHT // 16))
    WIN.blit(outline, (1/3 * blockSize + int(1/30 * blockSize), HEIGHT // 16))
    WIN.blit(outline, (1/3 * blockSize, HEIGHT // 16 - int(1/30 * blockSize)))
    WIN.blit(outline, (1/3 * blockSize, HEIGHT // 16 + int(1/30 * blockSize)))
    WIN.blit(text, (1/3 * blockSize, HEIGHT // 16))

def endscreen(color):
    if color == "black":
        WIN.blit(outline2, (3 * blockSize - int(1/30 * blockSize), HEIGHT // 2 - 1/3 * blockSize))
        WIN.blit(outline2, (3 * blockSize + int(1/30 * blockSize), HEIGHT // 2 - 1/3 * blockSize))
        WIN.blit(outline2, (3 * blockSize, HEIGHT // 2 - 1/3 * blockSize - int(1/30 * blockSize)))
        WIN.blit(outline2, (3 * blockSize, HEIGHT // 2 - 1/3 * blockSize + int(1/30 * blockSize)))
        WIN.blit(text2, (3 * blockSize, HEIGHT // 2 - 1/3 * blockSize))
    elif color == "white":
        WIN.blit(outline3, (3 * blockSize - int(1/30 * blockSize), HEIGHT // 2 - 1/3 * blockSize))
        WIN.blit(outline3, (3 * blockSize + int(1/30 * blockSize), HEIGHT // 2 - 1/3 * blockSize))
        WIN.blit(outline3, (3 * blockSize, HEIGHT // 2 - 1/3 * blockSize - int(1/30 * blockSize)))
        WIN.blit(outline3, (3 * blockSize, HEIGHT // 2 - 1/3 * blockSize + int(1/30 * blockSize)))
        WIN.blit(text3, (3 * blockSize, HEIGHT // 2 - 1/3 * blockSize))
