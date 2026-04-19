class Stone:
    COLOR_BLACK = 0
    COLOR_WHITE = 1
    COLOR_EMPTY = -1
    def __init__(self, color):
        self.north_stone = None
        self.east_stone = None
        self.south_stone = None
        self.west_stone = None
        self.color = color

    def getColor(self):
        return self.color
    
    def getChar(self):
        """Returns ASCII character corresponding to stone color"""
        if self.color == self.COLOR_BLACK:
            return "@"
        elif self.color == self.COLOR_WHITE:
            return "#"
        elif self.color == self.COLOR_EMPTY:
            return '+'
    