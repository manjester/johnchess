import pygame

from functions.pieces import *

# default = 504, 504
WIDTH, HEIGHT = 504, 504
blockSize = int(WIDTH / 8)

# initiate game window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Magchess")

# colors
Color1 = (118, 150, 86)
Color2 = (238, 238, 210)
Color1sel = (194, 68, 68)
Color2sel = (242, 107, 107)