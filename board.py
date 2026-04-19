from stone import *


class Board:
    def __init__(self, size):
        self.size = size
        self.__world = [[]]

        for y in range(size):
            for x in range(size): 
                self.__world[y].append(Stone(Stone.COLOR_EMPTY))
            self.__world.append([])

    def place_stone(self, posx, posy, stone: Stone):
        """Places stone object onto Board instance"""
        try:
            self.__world[posy][posx] = stone
        except IndexError:
            print("Error! Coordinate out of range.")

    def __str__(self):
        retval = ""
        for y in range(self.size):
            for x in range(self.size):
                char = self.__world[y][x].getChar()
                retval += char
            retval += '\n'
        return retval