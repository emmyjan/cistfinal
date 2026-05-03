from board import *
from game import *

def main():
    #Intitialize Game
    wb = Board(9, (222, 36), (759, 572))
    game = Game(wb)
    wb.set_game_controller(game)
    game.main_loop()

if __name__ == "__main__":
    main()