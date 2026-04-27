class Stone:
    COLOR_BLACK = 0
    COLOR_WHITE = 1
    COLOR_EMPTY = -1


    def __init__(self, posx, posy, color, name="Unnamed"):
        self.north_stone = None
        self.east_stone = None
        self.south_stone = None
        self.west_stone = None
        self.color = color
        self.__name = name
        self.__x = posx
        self.__y = posy


    def print_links(self):
        print(f"My name is {self.__name} and my color is {self.getChar()}")
        print("To the North is: ", end = '')
        print(self.north_stone)
        print("To the South is: ", end = '')
        print(self.south_stone)
        print("To the East is: ", end = '')
        print(self.east_stone)
        print("To the West is: ", end = '')
        print(self.west_stone)

    def getColor(self):
        return self.color
    
    def getLinks(self):
        """Returns a tuple of all linked stones, in directional order of NESW"""
        return (self.north_stone, self.east_stone, self.south_stone, self.west_stone)

    def getName(self):
        return self.__name

    def getChar(self):
        """Returns ASCII character corresponding to stone color"""
        if self.color == self.COLOR_BLACK:
            return "@"
        elif self.color == self.COLOR_WHITE:
            return "#"
        elif self.color == self.COLOR_EMPTY:
            return '+'
    
    def __str__(self):
        return (f"{self.__name}, color is {self.getChar()}!")
