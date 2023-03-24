import pygame
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
TURKISH = (0, 255, 255)
BLUE = (0, 0, 255)
PINK = (255, 0, 255)

FPS = 60

WIDTH, HEIGHT = 560, 710

ROWS = COLS = 28 #how many pixels

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = WHITE

DRAW_GRID_LINES = False #showing the grid or not

def get_font(size):
    return pygame.font.SysFont("comicsans", size)

def get_another_font(name, size):
    return pygame.font.SysFont(name, size)