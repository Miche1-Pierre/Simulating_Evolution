import pygame
import random

from Settings import *

class Food:
    def __init__(self, grid_width, grid_height, tilesize, color):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.tilesize = tilesize
        self.color = color
        self.food_positions = []


    # Draw random
    def spawn_food(self, food_count):
        self.food_positions = []

        for _ in range(food_count):
            x = random.randint(0, self.grid_width - 1)
            y = random.randint(0, self.grid_height - 1)
            self.food_positions.append((x, y))

    def draw_single_food(self):
        x = random.randint(0, self.grid_width - 1)
        y = random.randint(0, self.grid_height - 1)
        self.food_positions.append((x, y))

    # Draw lines
    def spawn_food_in_lines(self, num_lines, grid_width, grid_height):
        self.food_positions = []
 
        centre_x = grid_width // (num_lines + 1)
        centre_y = grid_height // (num_lines + 1)
 
        for i in range(1, num_lines + 1):
            y = (i * centre_y) - 1
            for x in range(grid_width):
                self.food_positions.append((x, y))
 
        for i in range(1, num_lines + 1):
            x = (i * centre_x) - 1
            for y in range(grid_height):
                self.food_positions.append((x, y))

    # Draw rectangle
    def spawn_food_rectangle(self, width, height, grid_width, grid_height):
        start_x = (grid_width - width) // 2
        start_y = (grid_height - height) // 2

        self.food_positions = []

        for x in range(start_x, start_x + width):
            for y in range(start_y, start_y + height):
                self.food_positions.append((x, y))


    def draw_food(self, screen,):
        for position in self.food_positions:
            x, y = position
            pygame.draw.rect(screen, self.color, (x * self.tilesize, y * self.tilesize, self.tilesize, self.tilesize))
