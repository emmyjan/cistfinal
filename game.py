from drawing import *
from board import *

class Game():
    TURN_BLACK = -1
    TURN_WHITE = 1
    TURN_SWITCH = -1
    TURN_NONE = 0
    """Contains the main loop"""
    def __init__(self, board: Board):
        self.board = board
        self.gamestate_turn = self.TURN_BLACK 
        self.drawer = Drawer(800, 600, board) # type: ignore
        self.running = True
        self.captured_white_stones = 0
        self.captured_black_stones = 0
    
    def main_loop(self):
        while self.running:
            self.process_events()
            self.drawer.draw_update()
        pygame.quit()
            
    def usr_clicked(self, event: pygame.Event):
        """Processes a user click. Gets mouse pos, will place a stone and\n change gamestate if successful,
        returning 0.\n Otherwise returns -1. event.type must == pygame.MOUSEBUTTONDOWN"""
        ind = self.board.mouse_to_index()
        if ind[0] == -1:
            return -1
        if self.board.get_stone(ind[1], ind[0]).color != Stone.COLOR_EMPTY:
            return -1
        if self.gamestate_turn != self.TURN_NONE:
            color = Stone.COLOR_BLACK if self.gamestate_turn == self.TURN_BLACK else Stone.COLOR_WHITE
            #TODO: Fix suicide bug
            # if self.board.get_group_liberties_pos(ind[1], ind[0], hypothetical_color=color) == 0:
            #     print("Ko-oops")
            #     return -1
            self.board.place_stone(ind[1], ind[0], color=color)
            self.gamestate_turn *= self.TURN_SWITCH
            return 0
        return -1
    
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.usr_clicked(event)

