import pygame
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
BLUE = (0, 165, 0)
GREEN = (0, 0, 170)
BROWN = (130, 90, 0)
LAVENDER = (220, 208, 255)

FPS = 60

WIDTH, HEIGHT = 600, 700

ROWS = COLS = 50

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH// COLS

BG_COLOR = WHITE

DRAW_GRID_LINES = True

def get_font(size):

    return pygame.font.SysFont("November Nan", size)