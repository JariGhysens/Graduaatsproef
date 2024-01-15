import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 121, 168)
RED = (255, 0, 0)
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('checkers/assets/crown.png'), (44, 25))
