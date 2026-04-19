import stone
from board_alt import *

wb = Board(5)
print(wb)

print("Liberties at 1,1")
print(wb.check_liberties(1, 1))
print(wb)
print(wb.calls_to_it, "calls holy wjat")
def play(color:int):
    color_str = "Black" if color == 1 else "White"
    x = int(input(f"{color_str} x: "))-1
    y = int(input(f"{color_str} y: "))-1

    
    
   
    try:
        wb.set_cord(x, y, color)
    except Exception as e:
        print("whoops!")
    wb.print_board()
    play(color*-1)

"""    for char in choice:
        if char.isnumeric:
            x = int(char)
            break

    for char in choice:
        if char.isnumeric:
            y = int(char)
            break
"""
