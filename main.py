from board import *


def main():
    test_stone = Stone(Stone.COLOR_BLACK)
    wb = Board(5)
    print(wb)
    wb.place_stone(2, 2, test_stone)
    print(wb)

if __name__ == "__main__":
    main()