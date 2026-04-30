import pygame
import stone
import board


class Drawer:
    """Controls the display of the game, draw_update is to be called during the main loop"""
    def __init__(self, w, h):
        self.WIDTH = w
        self.HEIGHT = h
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.__bg = pygame.image.load("board.png")
        pygame.init()

    def draw_update(self):
        self.screen.blit(self.__bg, (0, 0))
        pygame.display.flip()
        self.clock.tick(60)
