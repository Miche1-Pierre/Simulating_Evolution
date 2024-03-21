import pygame
import random

from Settings import *

class Microbes:
    def __init__(self, X, Y ):
        self.x = X
        self.y = Y
        self.color = MICROBE_COLOR
        self.direction = random.randint(0, 7)
        self.energy = MICROBE_START_ENERGY

    def draw_microbes(self, screen):
         pygame.draw.circle(screen, self.color, (int(self.x * TILESIZE + TILESIZE / 2), int(self.y * TILESIZE + TILESIZE / 2)), int(TILESIZE / 2))

    def move(self):
       direction_table = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
       dx, dy = direction_table[self.direction]
       self.x += dx
       self.y += dy
       self.energy -= MICROBE_ENERGY_LOSS_PER_TICK

    def evolve(self):
        genome = [random.random() for _ in range(8)]
        total_prob = sum(genome)
        prob_norm = [prob / total_prob for prob in genome]

        r = random.random()
        cumulative_prob = 0
        for i, prob in enumerate(prob_norm):
            cumulative_prob += prob
            if r < cumulative_prob:
                self.direction = (self.direction + i) % 8
                break

    def eat_food(self, food):
        if self.energy < MICROBE_MAX_ENERGY:
            self.energy += MICROBE_ENERGY_GAIN_PER_FOOD
            if self.energy >= MICROBE_REPRODUCE_ENERGY:
                return True
        if (self.x, self.y) in food.food_positions:
            food.food_positions.remove((self.x, self.y))
        return False

    def reproduce(self):
        self.energy /= 2
        return Microbes(self.x, self.y)