import pygame
import sys

from Settings import *
from Grid import *


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Life Simulator")

# Grid
grid = Grid(X_GRID, Y_GRID, TILESIZE)
grid.set_color(GRID_COLOR)

# Food

# Microbe


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(SCREEN_COLOR)

    grid.draw_grid(screen)

    pygame.display.flip()

pygame.quit()