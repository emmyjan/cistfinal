"""
DEPRECATED: Do not use, code remains to use samples in other files.
"""

import pygame
import background
import board
import stone

WIDTH = 800
HEIGHT = 600
GRID_LENGTH = (223, 760)
screen = None, clock = None


def init_game():
    global screen, clock
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    player_pos = pygame.Vector2(300, 400)
    bg = pygame.image.load("board_2.png")
    circles = []
    working_board = None

def conform_to_grid(grid_start_to_end: tuple, x, y, size) -> pygame.Vector2:
    """Snaps a coordinate to nearest point on a grid"""
    size_square = (grid_start_to_end[0] - grid_start_to_end[1]) // size
    stone_x = (x // size_square) * size_square
    stone_y = (y // size_square) * size_square

    if stone_x < grid_start_to_end[0]:
        stone_x = grid_start_to_end[0]
        # or stone_x > size_square[1]:
        stone_x
    return pygame.Vector2(stone_x, stone_y)


def draw_stone(stone: stone.Stone, x, y):
    if stone.getColor() == stone.COLOR_BLACK:
        pygame.draw.circle(screen, "black", (x, y), 25)
    elif stone.getColor() == stone.COLOR_WHITE:
        pygame.draw.circle(screen, "white", (x, y), 25)

def draw_board(board: board.Board, start_x, start_y):
    world = board.get_board()
    size = board.get_size()
    size_square = (GRID_LENGTH[1] - GRID_LENGTH[0]) // size
    
    for y in range(size):
        for x in range(size):
            print(start_x, start_y, "are thine cords")
            st = world[y][x]
            draw_stone(st, start_x, start_y)
            start_x += size_square
        start_y += size_square

def draw_loop():
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill("purple")

        screen.blit(bg, (0, 0))
        for pos in circles:
            pygame.draw.circle(screen, "black", pos, 25)
        pygame.draw.circle(screen, "red", player_pos, 15)
        
        if working_board != None:
            draw_board(working_board, 225, 24)
        # maddy was here and is cool n stuff

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_SPACE]:
            circles.append(conform_to_grid(GRID_LENGTH, player_pos.x, player_pos.y, 9))

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()