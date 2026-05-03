from drawing import *
from board import *

class Game():
    """Handles game logic. Contains the main loop."""
    TURN_BLACK = -1
    TURN_WHITE = 1
    TURN_SWITCH = -1
    TURN_NONE = 0
    
    def __init__(self, board: Board):
        self.board = board
        self.gamestate_turn = self.TURN_BLACK 
        self.drawer = Drawer(800, 600, board) # type: ignore
        self.drawer.set_game_controller(self)
        self.running = True
        self.captured_white_stones = 0
        self.captured_black_stones = 0
        self.last_player_pass = False
    
    def main_loop(self) -> None:
        """Main loop of the game. Runs until pygame is exited"""
        while self.running:
            self.process_events()
            self.drawer.update_scores((self.captured_white_stones, self.captured_black_stones))
            self.drawer.draw_update()
            self.call_turn_stone_draw()
        pygame.quit()
    
    def call_turn_stone_draw(self) -> None:
        """Tells Drawer instance to draw a sample stone of given color"""
        if self.gamestate_turn == Game.TURN_NONE:
            return
        if self.gamestate_turn == Game.TURN_BLACK:
            self.drawer.draw_current_turn_stone("black") 
        else:
            self.drawer.draw_current_turn_stone("white") 

    def usr_clicked(self, event: pygame.Event) -> int:
        """Processes a user click. Gets mouse pos, will place a stone and\n change gamestate if successful,
        returning 0.\n Otherwise returns -1. event.type must == pygame.MOUSEBUTTONDOWN"""
        ind = self.board.mouse_to_index() #Get index of stone clicked

        if ind[0] == -1: #Error case
            return -1
        if self.board.get_stone(ind[1], ind[0]).color != Stone.COLOR_EMPTY: #We can't place a stone on a full spot
            return -1
        if self.gamestate_turn != self.TURN_NONE: #Ensure game is still active
            color = Stone.COLOR_BLACK if self.gamestate_turn == self.TURN_BLACK else Stone.COLOR_WHITE #Color selection

            if self.board.get_group_liberties_pos(ind[1], ind[0], hypothetical_color=color) == 0: #If the selected spot is in danger...
                found_dead = False
                found_same = False

                #Check the linked stones to check edge cases
                for link in self.board.get_stone(ind[1], ind[0]).getLinks():
                    if link == None:
                        continue
                    if link.getColor() == color: #We found friendlies!
                        found_same = True
                    if self.board.get_group_liberties(link) <= 1 and link.getColor() != color: #If this linked stone is vulnerable to capture
                        found_dead = True

                if not found_dead and not found_same:
                    return -1 # Error case

            
            self.board.place_stone(ind[1], ind[0], color=color)
            self.change_turn()
            self.last_player_pass = False
            return 0
        
        return -1

    def change_turn(self) -> None:
        """Switches to the next player's turn"""
        self.gamestate_turn *= self.TURN_SWITCH
        self.drawer.flip_current_turn_color()
        self.drawer.set_game_msg("")

    def pass_button(self) -> None:
        """Functionality of the pass button. Ends game if called while last_player_pass is True"""
        if self.last_player_pass:
            
            self.drawer.set_game_msg("Game Over!")
            self.gamestate_turn = self.TURN_NONE
        else:
            self.change_turn()
            self.drawer.set_game_msg("Player Passes")
            self.last_player_pass = True
    
    def process_events(self) -> None:
        """Handler of pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.usr_clicked(event)
            if pygame.key.get_just_released()[pygame.K_p]:
                self.pass_button()

