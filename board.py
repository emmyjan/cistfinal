class Board:
    ST_WHITE = -1
    ST_BLACK = 1
    ST_NONE = 0
    ST_EDGE = 0
    ST_NEXTPOS = 1
    ST_NEXTNEG = -1
    ST_TEMP_BARRIER = -2
    def __init__(self, size_x: int, size_y: int):
        self.__world = []
        self.size_x = size_x
        self.size_y = size_y
        self.__salts = self.__world[:]
        for x in range(size_x):
            self.__world.append([])
            for y in range(size_y):
                self.__world[x].append(self.ST_NONE)

    def __parse(self, cord):
        if cord == self.ST_NONE:
            return '+'
        elif cord == self.ST_WHITE:
            return "@"
        elif cord == self.ST_BLACK:
            return "#" 

    def print_board(self):
        for x in range(self.size_x):
            for y in range(self.size_y):
                char = self.__parse(self.__world[x][y])
                print(f"{char}",end="")
            print()

    def set_cord(self, x:int, y:int , val: int):
        self.__world[y][x] = val

    def check_liberties(self, x, y, callee_self=False):
        liberties = 0
        COLOR = self.__world[y][x]
        if COLOR == self.ST_NONE:
            return 0
        
        if not (x + self.ST_NEXTPOS > self.size_x - 1):
            if self.__world[x+1][y] == self.ST_NONE:
                liberties += 1
            elif self.__world[x+1][y]
        

            