from pygame import *
HEIGHT = 600
WIDTH = 600
init()
screen = display.set_mode((WIDTH, HEIGHT))
font = font.SysFont(None, 100)

def box_text(text=""):
    global font 
    global screen   
    x = WIDTH // 2
    y = HEIGHT // 2
    rectangle = Rect(x-100, y+100, HEIGHT - int(HEIGHT*.35), WIDTH)
    draw.rect(screen, (255, 0, 0), rectangle)
    display = font.render(text, True, (0,0,255))
    screen.blit(display, (x-50, y-50))

def draw_grid(x1, y1, x2, y2, size):
    """Draws grid within box"""
    """
    distance = (x2 - x1) // size
    points_x = [(x)*distance for x in range(size)]
    points_y = [(y)*distance for y in range(size)]
    print(points_x)
    points = [(points_x[i], points_y[i]) for i in range(size)]
    
    print(points)
    draw.lines(screen, Color(255, 255, 255), True, (
        (points)
    ))
    """
    draw.lines(screen, Color(255, 255, 255), False, ((0,0,), (0, 100), (20, 100), (20, 0)), width = 3)
def main():
    global screen
    running = True
    while running:
        screen.fill("Gray")
        draw_grid(0, 0, 300, 300, 9)
        display.update()    

        for events in event.get():
    
            if events.type == QUIT:
                running = False

    exit()
if __name__ == "__main__":
    main()
