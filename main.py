from board import *


def main():
    wb = Board(5)
    print(wb)
    wb.place_stone(2, 2, name="Bobbiam")
    wb.place_stone(2, 1, name="Robbiam")
    # test that maddy can exist

    print(wb.get_group_liberties(2,2))
    print(wb)

if __name__ == "__main__":
    main()