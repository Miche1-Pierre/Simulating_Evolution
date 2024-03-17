import pygame
import random

from Settings import *

class Microbes:
    def __init__(self, X, Y ):
        self.x = X
        self.y = Y
        self.color = MICROBE_COLOR
        self.direction = random.randint(0, 7)

    def draw_microbes(self, screen):
         pygame.draw.circle(screen, self.color, (int(self.x * TILESIZE + TILESIZE / 2), int(self.y * TILESIZE + TILESIZE / 2)), int(TILESIZE / 2))


    def move(self):
       # Tableau des mouvements possibles en fonction de la direction
       motion_table = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
       dx, dy = motion_table[self.direction]
       self.x += dx
       self.y += dy

    def evolve(self):
        # Génome représentant les probabilités de changement de direction
        genome = [random.random() for _ in range(8)]
        total_prob = sum(genome)
        # Normalisation des probabilités pour que leur somme soit égale à 1
        prob_norm = [prob / total_prob for prob in genome]

        # Sélection aléatoire d'une direction en fonction des probabilités du génome
        r = random.random()
        cumulative_prob = 0
        for i, prob in enumerate(prob_norm):
            cumulative_prob += prob
            if r < cumulative_prob:
                self.direction = (self.direction + i) % 8
                break