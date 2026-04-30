from drawing import *


class Game():
    def __init__(self):
        self.drawer = Drawer(800, 600)
        self.running = True

    def main_loop(self):
        while self.running:
            self.process_events()
            self.drawer.draw_update()

        pygame.quit()
            
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False