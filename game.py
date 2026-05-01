import pygame.constants
from drawing import *


class Game():
    """Contains the main loop"""
    def __init__(self, board):
        self.board = board

        self.drawer = Drawer(800, 600, board)
        self.running = True
        
    def main_loop(self):
        while self.running:
            self.process_events()
            self.drawer.draw_update()

        pygame.quit()

    def click(self, event):
        # idfk place a stone or some shit please help I'm having a mental breakdown

        if pygame.get_mouse_pos ifgknljnlknvgkvjfdrnekyjnhgfkhjbliejzerllkmlk

            
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.constants.MOUSEBUTTONDOWN:
                self.click(event)
