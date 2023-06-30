import pygame , sys, os

map_1 = [
"1111111111111111111111",
"2         N02       W0",
"2 M  XX   XX2 R  E R53X",
"X34  02    02  4536  0",
"2   M02 M  02 R E  RM0",
"2  34XX34  02  4536  0",
"2 M  02   M02 R E  RM0",
"X34  02  34XX  4536  0",
"2   M02   R E  R    N0",
"2p  XXX  E 4536    XX0",
"1111111111111111111111",
]

size_plataforma = 64
SCREEN_WIDTH = 1406
SCREEN_HEIGHT = 704
CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
CLOSE = (SCREEN_WIDTH // 0.5, SCREEN_HEIGHT // 0.5)
FPS = 30
SPEED = 10
SPEED_ENEMY = 8

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
MAGENTA = (255,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)

