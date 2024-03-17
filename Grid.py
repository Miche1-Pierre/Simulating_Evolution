import pygame

from Settings import *

class Grid:
    def __init__(self, X, Y, tilesize):
        self.X = X
        self.Y = Y
        self.tilesize = tilesize

    def set_color(self, color):
        self.color = color

    def draw_grid(self, screen):
        for i in range(1, self.X):
            pygame.draw.line(screen, self.color, (self.tilesize * i, 0), (self.tilesize * i, self.tilesize * self.X))
        for i in range(1, self.Y):
            pygame.draw.line(screen, self.color, (0, self.tilesize * i), (self.tilesize * self.X, self.tilesize * i))
            