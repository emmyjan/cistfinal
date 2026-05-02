from stone import *
from math import *
import pygame
import game


class Board:
    def __init__(self, size: int, board_start=(-1,-1), board_end=(-1,-1)):
        self.size = size
        self.__world = [[]]
        self.__slist = [] #Positions already visited by get_group_liberties
        self.board_start = board_start
        self.board_end = board_end #Coordinates of the board on the screen
        self.intersections = self.get_instersections()
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

    def get_instersections(self) -> tuple:
        SIZE = 67
        y_list = []
        x_list = []
        for y in range(self.size):
            for x in range(self.size):
                cord = self.board_start
                x_list.append((cord[0] + (SIZE*x), cord[1] + (SIZE*y)))
            y_list.append(x_list[:])
            x_list = []
        return y_list
    
    def check_death(self, stone:Stone):
        """Determines if a stone or its neighbors are dead"""
        if self.get_group_liberties(stone) == 0:
            if stone.getColor() == Stone.COLOR_WHITE:
                game.captured_white_stones += self.delete_group(stone)
            elif stone.getColor() == Stone.COLOR_BLACK:
                game.captured_black_stones += self.delete_group(stone)
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

    def set_game(self, gayme):
        gayme.Game

    def __str__(self):
        retval = ""
        for y in range(self.size):
            for x in range(self.size):
                char = self.__world[y][x].getChar()
                retval += char
            retval += '\n'
        return retval

    def snap_to_grid(self, x, y) -> tuple:
        """Alligns a coordinate to the closest intersection"""
        square_size = (self.board_end[0] - self.board_start[0]) // self.size
        square_size = 66

        print(f"Square size: {square_size}, sq*{self.size} = {square_size*self.size}")
        new_x = ((x / square_size )* square_size)
        new_y = ((y / square_size )* square_size)

        return (new_x, new_y)
    
    def mouse_to_index(self) -> tuple:
        """Gets index of nearest intersection in self.intersections\n
        Returns (-1,-1) if mouse out of range
        """
        TOLERANCE = 30
        OFFSET = 28
        ms = pygame.mouse.get_pos()
        x = ms[0]
        y = ms[1]

        x_ind = -1
        y_ind = -1

        if x + TOLERANCE < self.board_start[0] or y + TOLERANCE < self.board_start[1]:
            return (-1, -1) #Out of range
        elif x - TOLERANCE > self.board_end[0] or y - TOLERANCE > self.board_end[1]:
            return (-1, -1) #Out of range
        
        #Go through intersections to find nearest index.
        for ind_r, row in enumerate(self.intersections):
            for ind_el, elem in enumerate(row):
                if x - OFFSET < elem[0] and y - OFFSET < elem[1]:
                    x_ind = ind_el
                    y_ind = ind_r
                    return (y_ind, x_ind)

        return (y_ind, x_ind)

    def get_group_liberties_pos(self, posx, posy, hypothetical_color=Stone.COLOR_EMPTY):
        stone = self.__world[posy][posx]
        return self.get_group_liberties(stone, hypothetical_color=Stone.COLOR_EMPTY)

    def call_flood_fill_stone(self, st: Stone, friendly_color=Stone.COLOR_BLACK):
        """Returns number of spaces in area. Returns negative if stone that is not a friendly_color is touched"""
        return self.flood_fill_stone(st, friendly_color=friendly_color, visited=[])

    def flood_fill_stone(self, st: Stone, friendly_color=Stone.COLOR_BLACK, visited=[]) -> int:
        """Do not call. Use call_flood_fill_stone. \nReturns number of spaces in area. Returns negative if stone that is not a friendly_color is touched"""
        spaces = 1 if (st.color == Stone.COLOR_EMPTY) else 0
        opposite_color = Stone.COLOR_WHITE if friendly_color == Stone.COLOR_BLACK else Stone.COLOR_BLACK         
        visited.append(st)

        if st.color != Stone.COLOR_EMPTY:
            return 0
        
        for link in st.getLinks():
            if link == None:
                continue
            cl = link.getColor()
            if cl == opposite_color:
                return -999
            elif cl == st.COLOR_EMPTY and link not in visited:
                spaces += self.flood_fill_stone(link, visited=visited)

        return spaces

    def delete_group(self, stone: Stone, visited=[]):
        """Deletes a group of stones, starting on any given Stone object"""
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
                deleted += self.delete_group(link, visited=visited)
        return deleted

    def get_group_liberties(self, stone: Stone, origin = True, hypothetical_color=Stone.COLOR_EMPTY):
        """Returns total number of liberties for a group at a specified coordinate\n
        hypothetical_color: Get the 'What If' Liberties if a Stone was a different color
        """
        if stone == None:
            return
        liberties = 0
        color = stone.getColor()

        if hypothetical_color != Stone.COLOR_EMPTY:
            color = hypothetical_color
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
            elif link.getColor() == color and link not in self.__slist:
                    liberties += self.get_group_liberties(link, origin=False)
                
        return liberties
    
