import random


class Board:

    ST_WHITE = -1
    ST_BLACK = 1
    ST_NONE = 0
    ST_SALT_EMPTY = -2
    ST_SALT_FRIENDLY = 2
    def __init__(self, size):
        self.size = size
        self.calls_to_it = 0

        self.__world = [[]]
        self.__salts = None
        for y in range(size):
            for x in range(size):
                apint = random.randint(-1, 1)
                self.__world[y].append(apint)
            self.__world.append([])

    def parse(self, cord):
        if cord == self.ST_NONE:
            return '+'
        elif cord == self.ST_WHITE:
            return "@"
        elif cord == self.ST_BLACK:
            return "#" 
        elif cord == 2:
            return '%'
        elif cord == -2:
            return '-'
        else:
            return "ERROR"
    def pos_to_id(self, x, y) -> int:
        """Deprecated"""
        if x > self.size or y > self.size:
            return -1
        y *= self.size
        return x + y
    
    def get_value(self, x, y):
        """Deprecated"""
        print(self.pos_to_id(x,y))
        return self.__world[self.pos_to_id(x, y)]

    def __alg_libs_iter(self, x, y):
        #Setup vars
        ST_SALT_EMPTY = -2
        ST_SALT_FRIENDLY = 2
        ST_FRIENDLY = self.ST_BLACK if self.__world[y][x] == self.ST_BLACK else self.ST_WHITE
        liberties = 0
        if self.__world[y][x] == self.ST_NONE:
            return -1
        self.__salts = []
        for i in range(self.size):
            self.__salts.append([x for x in self.__world[i]])
        
        #Begin main loop
        while True:
            if x+1 < self.size:
                if self.__salts[y][x+1] == self.ST_NONE:
                    print(f"Found one at {y},{x+1}")
                    liberties += 1
                    self.__salts[y][x+1] = ST_SALT_EMPTY
            if y+1 < self.size:
                if self.__salts[y+1][1] == self.ST_NONE:
                    print(f"Found one at {y+1},{x}")                
                    liberties += 1
                    self.__salts[y+1][x] = ST_SALT_EMPTY
            if x-1 >= 0:
                if self.__salts[y][x-1] == self.ST_NONE:
                    print(f"Found one at {y},{x-1}")
                    liberties += 1
                    self.__salts[y][x-1] = ST_SALT_EMPTY            

    def __alg_libs(self, x, y, origin=False, depth=0):
        self.calls_to_it += 1
        print(f"\n\nFresh new call! depth is {depth}")
        ST_SALT_EMPTY = -2
        ST_SALT_FRIENDLY = 2
        ST_FRIENDLY = self.ST_BLACK if self.__world[y][x] == self.ST_BLACK else self.ST_WHITE
        liberties = 0
        if self.__world[y][x] == self.ST_NONE:
            return -1
        if origin:
            self.__salts = []
            for i in range(self.size):
                self.__salts.append([x for x in self.__world[i]])

        if self.__salts is self.__world:
            print("NONO")
        print(f"Troweling {x},{y}! Its status is {self.__salts[y][x]}, depth is {depth}")

        if depth > 7:
            return liberties
        self.__salts[y][x] = ST_SALT_FRIENDLY
        #First, count the adjacent empty spots.
        if x+1 < self.size:
            if self.__salts[y][x+1] == self.ST_NONE:
                print(f"Found one at {y},{x+1}")
                liberties += 1
                self.__salts[y][x+1] = ST_SALT_EMPTY
        if y+1 < self.size:
            if self.__salts[y+1][1] == self.ST_NONE:
                print(f"Found one at {y+1},{x}")                
                liberties += 1
                self.__salts[y+1][x] = ST_SALT_EMPTY
        if x-1 >= 0:
            if self.__salts[y][x-1] == self.ST_NONE:
                print(f"Found one at {y},{x-1}")
                liberties += 1
                self.__salts[y][x-1] = ST_SALT_EMPTY
        if y-1 >= 0:
            if self.__salts[y-1][x] == self.ST_NONE:
                print(f"Found one at {y-1},{x}")
                liberties += 1
                self.__salts[y-1][x] = ST_SALT_EMPTY
        
        #Next, jump into friendly spots
        if x+1 < self.size:
            if self.__salts[y][x+1] == ST_FRIENDLY:
                liberties += self.__alg_libs(x+1, y, depth=depth+1)
        if y+1 < self.size:
            if self.__salts[y+1][1] == ST_FRIENDLY:
                liberties += self.__alg_libs(x, y+1,depth=depth+1)
        if x-1 >= 0:
            if self.__salts[y][x-1] == ST_FRIENDLY:
                liberties += self.__alg_libs(x-1, y, depth=depth+1)
        if y-1 >= 0:
            if self.__salts[y-1][x] == ST_FRIENDLY:
                liberties += self.__alg_libs(x, y-1, depth=depth+1)

        #Finally, traverse through already-visited spots to search for more
        if x+1 < self.size:
            if self.__salts[y][x+1] == ST_SALT_FRIENDLY:
                liberties += self.__alg_libs(x+1, y, depth=depth+1)
        elif y+1 < self.size:
            if self.__salts[y+1][1] == ST_SALT_FRIENDLY:
                liberties += self.__alg_libs(x, y+1,depth=depth+1)
        elif x-1 >= 0:
            if self.__salts[y][x-1] == ST_SALT_FRIENDLY:
                liberties += self.__alg_libs(x-1, y, depth=depth+1)
        elif y-1 >= 0:
            if self.__salts[y-1][x] == ST_SALT_FRIENDLY:
                liberties += self.__alg_libs(x, y-1, depth=depth+1)

        if origin:
            self.print_board(self.__salts)
            self.__salts = []
        print(f"Am I the original? {origin}. Returning {liberties}.")
        return liberties
    def check_liberties(self, x, y):
        return self.__alg_libs(x, y, True)

    def __str__(self):
        retval = ""
        for y in range(self.size):
            for x in range(self.size):
                char = self.parse(self.__world[y][x])
                retval += char
            retval += '\n'
        return retval

    def print_board(self, board):
        retval = ""
        for y in range(self.size):
            for x in range(self.size):
                char = self.parse(board[y][x])
                retval += char
            retval += '\n'
        print( retval)        
"""
    def __str__(self):
        retval = ""
        for x in range(self.size):
            for y in range(self.size):
                cord = self.pos_to_id(x, y)
                char = self.parse(self.__world[cord])
                retval += f"{char}"
            retval += '\n'
        return retval
"""
    