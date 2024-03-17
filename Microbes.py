import pygame

from Settings import *

class Microbes:
    def __init__(self, X, Y ):
        self.x = X
        self.y = Y
        self.color = MICROBE_COLOR

    def draw_microbes(self, screen):
         pygame.draw.circle(screen, self.color, (int(self.x * TILESIZE + TILESIZE / 2), int(self.y * TILESIZE + TILESIZE / 2)), int(TILESIZE / 2))