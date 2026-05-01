import pygame
import stone
import board


class Drawer:
    """Controls the display of the game, draw_update is to be called during the main loop"""
    def __init__(self, w, h, board):
        self.WIDTH = w
        self.HEIGHT = h
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.board = board
        self.__bg = pygame.image.load("board.png")
        self.set_board_params( (228, 25), (760, 569))
        pygame.init()

    def set_board_params(self, start_coord: tuple, end_coord: tuple):
        self.start_coord = start_coord
        self.end_coord = end_coord

    def draw_update(self) -> None:
        self.screen.blit(self.__bg, (0, 0))
        self.draw_board()
        self.draw_highlight()
        pygame.display.flip()
        self.clock.tick(60)

    def draw_board(self) -> None:
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

    def draw_highlight(self) -> None:



        size_square = (self.end_coord[0] - self.start_coord[0]) // self.board.get_size()
        boxx = (pygame.mouse.get_pos()[0] // size_square) * size_square
        boxy = (pygame.mouse.get_pos()[1] // size_square) * size_square
        box = pygame.Rect(boxx,boxy,30,30)
        if pygame.mouse.get_pos()[0] < self.start_coord[0] or pygame.mouse.get_pos()[1] > self.end_coord[1]:
            return
        else:
            pygame.draw.rect(self.screen, "blue", box, 1)




