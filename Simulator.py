import pygame
import sys

from Settings import *
from Grid import *
from Food import *
from Microbes import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Life Simulator")

# Grid
grid = Grid(X_GRID, Y_GRID, TILESIZE)
grid.set_color(GRID_COLOR)

# Food
food = Food(X_GRID, Y_GRID, TILESIZE, FOOD_COLOR)
food.spawn_food(FOOD_INITIAL_COUNT)

# Microbe
microbes = [Microbes(random.randint(0, X_GRID - 1), random.randint(0, Y_GRID - 1)) for _ in range(MICROBE_COUNT)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(SCREEN_COLOR)

    # Grid
    grid.draw_grid(screen)

    # Food
    food.draw_food(screen)
    for _ in range(FOOD_SPAWN_RATE):
        food.draw_single_food()

    # Microbe
    for microbe in microbes:
        microbe.draw_microbes(screen)
        microbe.move()
        microbe.evolve()

    pygame.display.flip()

pygame.quit()