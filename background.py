import pygame

class Background(pygame.sprite.Sprite):
    W = 800
    H = 600

    def __init__(self, filename):
        super().__init__(self)

        with open(filename, 'r') as img:
            self.image = pygame.image.load(img)




        