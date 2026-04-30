from board import *
from game import *

def main():
    wb = Board(5)
    print(wb)
    wb.place_stone(2, 2, name="Bobbiam")
    wb.place_stone(2, 1, name="Robbiam")
    wb.place_stone(1, 1, name="Lobbiam")
    wb.place_stone(0, 1, name="Clobbiam")
    # test that maddy can exist
    print(wb.get_group_liberties_pos(2,2))
    print(wb)

    game = Game()
    game.main_loop()
    

if __name__ == "__main__":
    main()