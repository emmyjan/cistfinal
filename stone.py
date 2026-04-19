class Stone:
    __stone_id_count = 0
    board_stones = []
    placeholder_hell = None
    def __init__(self):
        self.__pos = None
        self.__color = None
        self.__group = None
        self.__liberties = 4
        self.__id = self.__stone_id_count
        self.__stone_id_count += 1

    def capture(self):
        self.__pos = self.placeholder_hell

    def get_id(self):
        return self.__id