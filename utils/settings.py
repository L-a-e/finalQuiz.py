import pygame
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 91, 97)
BLUE = (136, 230, 136)
GREEN = (70, 150, 216)
BROWN = (196, 164, 132)
LAVENDER = (170, 152, 169)

FPS = 60

WIDTH, HEIGHT = 600, 700

ROWS = COLS = 50

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH// COLS

BG_COLOR = WHITE

DRAW_GRID_LINES = True

def get_font(size):

    return pygame.font.SysFont("November Nan", size)