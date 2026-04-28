import pygame
import background
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(300, 400)
bg = pygame.image.load("board.png")
circles = []

def conform_to_grid(grid_start_x, grid_end_x, x, y, size) -> pygame.Vector2:
    """Snaps a coordinate to nearest point on a grid"""
    size_square = (grid_start_x - grid_end_x) // size
    stone_x = (x // size_square) * size_square
    stone_y = (y // size_square) * size_square
    return pygame.Vector2(stone_x, stone_y)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("purple")

    screen.blit(bg, (0, 0))
    for pos in circles:
        pygame.draw.circle(screen, "black", pos, 25)
    pygame.draw.circle(screen, "red", player_pos, 15)
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
        circles.append(conform_to_grid(223, 760, player_pos.x, player_pos.y, 9))

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()