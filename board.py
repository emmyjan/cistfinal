from stone import *


class Board:
    def __init__(self, size):
        self.size = size
        self.__world = [[]]

        for y in range(size):
            for x in range(size): 
                self.__world[y].append(Stone(x, y, Stone.COLOR_EMPTY, name = "Unnamed"))

            self.__world.append([])

        self.establish_world_links()

    def establish_world_links(self):
        for y in range(self.size):
            for x in range(self.size):
                if y - 1 >= 0:
                    self.__world[y][x].north_stone = self.__world[y-1][x]
                if x - 1 >= 0:
                    self.__world[y][x].west_stone = self.__world[y][x-1]
                if y + 1 < self.size:
                    self.__world[y][x].south_stone = self.__world[y+1][x]
                if x + 1 < self.size :
                    self.__world[y][x].east_stone = self.__world[y][x+1]

    def place_stone(self, posx, posy, name="Unnamed", color=Stone.COLOR_WHITE):
        """Places new stone object onto Board instance"""
        try:
            self.__world[posy][posx] = Stone(posx, posy, color, name)
            self.establish_world_links()
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

    def get_group_liberties(self, posx, posy):
        """Returns total number of liberties for a group at a specified coordinate"""
        stone = self.__world[posy][posx]
        slist.append(posx, posy)
        liberties = 0
        for link in stone.getLinks():
            if link == None:
                continue
            if link.getColor() == Stone.COLOR_EMPTY:
                if (check spot) !in llist:
                    llist.append()
                    liberties += 1
            elif link.getColor() == stone.getcolor() and (position of stone) !in wlist:
                get_group_liberties(self, location of said stone)
        return liberties
