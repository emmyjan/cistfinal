import pygame
import stone
import board

class Drawer:
    """Controls the display of the game, draw_update is to be called during the main loop"""
    def __init__(self, w, h, board: board.Board):
        pygame.init()
        self.WIDTH = w
        self.HEIGHT = h
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.board = board
        self.__bg = pygame.image.load("board_2.png")
        self.game_controller = None
        self.game_over_msg = False
        self.game_msg = ""
        self.current_turn_color = "black"
        self.font = pygame.font.Font(None, 32)
        self.scores = (0,0)
        self.set_board_params( (220, 30), (760, 575))

    def update_scores(self, score: tuple) -> None:
        self.scores = score[:]

    def set_game_controller(self, gm):
        self.game_controller = gm

    def set_board_params(self, start_coord: tuple, end_coord: tuple):
        self.start_coord = start_coord
        self.end_coord = end_coord

    def flip_current_turn_color(self):
        if self.current_turn_color == "black":
            self.current_turn_color = "white"
        else:
            self.current_turn_color = "black"

    def draw_update(self) -> None:
        self.screen.blit(self.__bg, (0, 0))
        self.draw_board()
        self.draw_current_turn_stone(self.current_turn_color)
        self.draw_scores()
        self.display_gamestate_msg()
        # if self.game.gamestate_turn == self.game.TURN_BLACK:
        #     pygame.draw.circle(self.screen, "black", (30, 30), 30)
        # else:
        #     pygame.draw.circle(self.screen, "black", (30, 30), 30)

        # self.draw_highlight()
        # testcoord = self.board.snap_to_grid(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        # pygame.draw.circle(self.screen, "purple", testcoord, 25)
       # pygame.draw.circle()
        # for y in range(9):
        #     for x in range(9):
        #         pygame.draw.circle(self.screen, "white", self.board.intersections[y][x], 28)
        pygame.display.flip()
        self.clock.tick(60)

    def set_game_msg(self, msg: str):
        self.game_msg = msg

    def display_gamestate_msg(self):
        message = self.font.render(f"{self.game_msg}", False, (10, 10, 10))
        self.screen.blit(message, (27, 411)) 

    def draw_board_dep(self) -> None:
        """Draws stones from board's world list.\n
        Requires start and end coord of in-game display board"""
        current_coord = list(self.start_coord[:])
        board_ptr = self.board.get_board() #Create a reference to the world board
        MAGIC_NUMBER = 1.27 #what

        size = len(board_ptr)
        space_size = (self.end_coord[0] - self.start_coord[0]) // size # Get distance between the intersections  
        for pos_y, y_dim in enumerate(board_ptr):
            for pos_x, x_dim in enumerate(y_dim):
                color = ""
                stone_color = board_ptr[pos_y][pos_x].getColor()
                current_coord = [self.start_coord[0] + pos_x * space_size *MAGIC_NUMBER, self.start_coord[1] + pos_y * space_size *MAGIC_NUMBER]
                if stone_color == stone.Stone.COLOR_EMPTY: #Determine cirlce color
                    continue
                elif stone_color == stone.Stone.COLOR_WHITE:
                    color = "white"
                else:
                    color = "black" 

                pygame.draw.circle(self.screen, color, current_coord, 25)

    def draw_board(self) -> None:
        """Draws stones from board's world list.\n
        Requires start and end coord of in-game display board"""
        color = "red"
        for ind_y, y in enumerate(self.board.get_board()):
            for ind_x, st in enumerate(y):
                if st.getColor() == stone.Stone.COLOR_EMPTY: #Determine cirlce color
                    continue
                elif st.getColor() == stone.Stone.COLOR_WHITE:
                    color = "white"
                else:
                    color = "black" 
                pygame.draw.circle(self.screen, color, self.board.intersections[ind_y][ind_x], 28)

    def draw_score(self) -> None:
        pygame.display.set_caption(self.game.captured_white_stones)
        pygame.freetype.SysFont("Arial")

    def draw_highlight(self) -> None:
        """Draws outline of square over nearest intersection to cursor"""
        OFFSET_X = 5
        OFFSET_Y = 20
        BOX_SIZE = 30

        size_square = (self.end_coord[0] - self.start_coord[0]) // (self.board.get_size()-1)
        boxx = (pygame.mouse.get_pos()[0] // size_square) * size_square + OFFSET_X
        boxy = (pygame.mouse.get_pos()[1] // size_square) * size_square + OFFSET_Y
        box = pygame.Rect(boxx,boxy,BOX_SIZE,BOX_SIZE)

        #Out of bounds check
        if pygame.mouse.get_pos()[0] < self.start_coord[0] or pygame.mouse.get_pos()[1] > self.end_coord[1]:
            return
        else:
            pygame.draw.rect(self.screen, "black", box, 1)

    def draw_current_turn_stone(self, color: str):
        CIRCLE_POS = (92, 375)
        CIRCLE_SIZE = 25
        
        pygame.draw.circle(self.screen, color, CIRCLE_POS, CIRCLE_SIZE) 

    def draw_scores(self):
        """Draws score of captured stones"""
        b_score = self.scores[1]
        w_score = self.scores[0]
        b_txt = self.font.render(f"{b_score}", False, (10, 10, 10))
        w_text = self.font.render(f"{w_score}", False, (10,10,10))
        self.screen.blit(b_txt, (94, 107)) 
        self.screen.blit(w_text, (94, 262))

