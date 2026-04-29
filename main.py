from board import *
import window

def main():
    wb = Board(5)
    print(wb)
    wb.place_stone(2, 2, name="Bobbiam")
    wb.place_stone(2, 1, name="Robbiam")
    wb.place_stone(1, 1, name="Lobbiam")
    wb.place_stone(0, 1, name="Clobbiam")
    window.working_board = wb
    # test that maddy can exist
    window.mainloop()
    print(wb.get_group_liberties_pos(2,2))
    print(wb)
    

if __name__ == "__main__":
    main()