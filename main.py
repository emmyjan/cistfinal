from board import *
from game import *

def main():
    wb = Board(9)
    print(wb)
    testing = False
    t = True
    if testing:
        while True:
            color = Stone.COLOR_BLACK if t else Stone.COLOR_WHITE
            print(wb)
            print(f"Player {color} to play.")

            x_cord = int(input("Enter x:"))
            y_cord = int(input("Enter y:"))

            if wb.get_stone(x_cord, y_cord).color != Stone.COLOR_EMPTY:
                print("Error! Occupied")
            else:
                wb.place_stone(x_cord, y_cord, color=color)
                print(f"Placing stone at {x_cord},{y_cord}.")

            t = not t
            color = not color
    # test that maddy can exist
    print(wb)

    game = Game(wb)
    game.main_loop()
    

if __name__ == "__main__":
    main()