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

# Food Random
food_random = Food(X_GRID, Y_GRID, TILESIZE, FOOD_COLOR)
food_random.spawn_food(FOOD_INITIAL_COUNT)
# Food Lines
food_lines = Food(X_GRID, Y_GRID, TILESIZE, FOOD_COLOR)
food_lines.spawn_food_in_lines(LINES_NUMBER, X_GRID, Y_GRID)
# Food Rectangle
food_rectangle = Food(X_GRID, Y_GRID, TILESIZE, FOOD_COLOR)
food_rectangle.spawn_food_rectangle(200, 200, X_GRID, Y_GRID)

# Microbe
microbes = [Microbes(random.randint(0, X_GRID - 1), random.randint(0, Y_GRID - 1)) for _ in range(MICROBE_COUNT)]

current_module = "draw random"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                current_module = "draw random"
            elif event.key == pygame.K_b:
                current_module = "draw lines"
            elif event.key == pygame.K_c:
                current_module = "draw rectangle"

    screen.fill(SCREEN_COLOR)

    # Grid
    grid.draw_grid(screen)

    # Different module (change food generation)
    # Random
    if current_module == "draw random":
        # Food
        food_random.draw_food(screen)
        for _ in range(FOOD_SPAWN_RATE):
            food_random.draw_single_food()

        # Microbe
        new_microbes = []
        for microbe in microbes:
            microbe.move()
            microbe.evolve()
            if (microbe.x, microbe.y) in food_random.food_positions:
                if microbe.eat_food(food_random):
                    new_microbes.append(microbe.reproduce())
            microbe.draw_microbes(screen)
            if microbe.energy <= 0:
                microbes.remove(microbe)
        microbes.extend(new_microbes)

    # Lines
    elif current_module == "draw lines":
        # Food
        food_lines.draw_food(screen)
        for _ in range(FOOD_SPAWN_RATE_LINES):
            food_lines.draw_single_food()
        
        # Microbe
        new_microbes = []
        for microbe in microbes:
            microbe.move()
            microbe.evolve()
            if (microbe.x, microbe.y) in food_lines.food_positions:
                if microbe.eat_food(food_lines):
                    new_microbes.append(microbe.reproduce())
            microbe.draw_microbes(screen)
            if microbe.energy <= 0:
                microbes.remove(microbe)
        microbes.extend(new_microbes)
    
    # Rectangle
    elif current_module == "draw rectangle":
        # Food
        food_rectangle.draw_food(screen)
        for _ in range(FOOD_SPAWN_RATE_RECTANGLE):
            food_rectangle.draw_single_food()

        # Microbe
        new_microbes = []
        for microbe in microbes:
            microbe.move()
            microbe.evolve()
            if (microbe.x, microbe.y) in food_rectangle.food_positions:
                if microbe.eat_food(food_rectangle):
                    new_microbes.append(microbe.reproduce())
            microbe.draw_microbes(screen)
            if microbe.energy <= 0:
                microbes.remove(microbe)
        microbes.extend(new_microbes)

    pygame.display.flip()

pygame.quit()