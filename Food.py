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

    def draw_food(self, screen):
        for position in self.food_positions:
            x, y = position
            pygame.draw.rect(screen, self.color, (x * self.tilesize, y * self.tilesize, self.tilesize, self.tilesize))
