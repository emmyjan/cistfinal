from stone import *


class Board:
    def __init__(self, size):
        self.size = size
        self.__world = [[]]
        self.__slist = [] #Positions already visited by get_group_liberties
        self.__dlist = [] #Positions already visited by delete_group
        
        self.NULL_STONE = Stone(-1, -1, Stone.COLOR_EMPTY, "NULL")

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

    def check_death(self, stone:Stone):
        """Determines if a stone or its neighbors are dead"""
        if self.get_group_liberties(stone) == 0:
            self.delete_group(stone)
        for link in stone.getLinks():
            if self.get_group_liberties(link) == 0:
                self.delete_group(link)

    

    def place_stone(self, posx, posy, name="Unnamed", color=Stone.COLOR_WHITE) -> Stone:
        """Places new stone object onto Board instance"""
        try:
            self.__world[posy][posx] = Stone(posx, posy, color, name)
            self.establish_world_links()
            self.check_death(self.__world[posy][posx])
            return self.__world[posy][posx]
        except IndexError:
            print("Error! Coordinate out of range.")
        return self.NULL_STONE
    
    def get_stone(self, x, y) -> Stone:
        """Finds Stone object at coordinates. Returns NULL_STONE if IndexError"""
        try:
            st = self.__world[y][x]
        except IndexError:
            print("Error! Index out of bounds in get_stone")
            return self.NULL_STONE
        return st

    def get_board(self):
        return self.__world
    
    def get_size(self):
        return self.size
    
    def __str__(self):
        retval = ""
        for y in range(self.size):
            for x in range(self.size):
                char = self.__world[y][x].getChar()
                retval += char
            retval += '\n'
        return retval

    def get_group_liberties_pos(self, posx, posy):
        stone = self.__world[posy][posx]
        return self.get_group_liberties(stone)

    def delete_group(self, stone: Stone, visited=[]):
        if stone == None:
            return
        if stone.getColor() == Stone.COLOR_EMPTY:
            return
        color = stone.getColor()
        visited.append(stone)
        stone.color = Stone.COLOR_EMPTY
        # adds the stones location to a list
        for link in stone.getLinks():
            if link == None:
                continue
                # error case
            if link.getColor() == color and link not in visited:
                # checks the spot being looked at to see if it is not in the list
                self.delete_group(link, visited=visited)







    def get_group_liberties(self, stone: Stone, origin = True):
        """Returns total number of liberties for a group at a specified coordinate"""
        if stone == None:
            return
        liberties = 0

        if origin:
            self.__slist = []

        self.__slist.append(stone)
        # adds the stones location to a list
        for link in stone.getLinks():
           
            if link == None:
                continue
                # error case

            if link.getColor() == Stone.COLOR_EMPTY and link not in self.__slist:
                # checks the spot being looked at to see if it is not in the list
                self.__slist.append(link)
                #adds the empty spot to the list
                liberties += 1
            elif link.getColor() == stone.getColor() and link not in self.__slist:
                    liberties += self.get_group_liberties(link, origin=False)
                
        return liberties
    
