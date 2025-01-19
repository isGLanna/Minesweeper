from Rank import insert_player


class Player:
    def __init__(self):
        self.__name = None
        self.__time = 0
        self.level = 0

    def set_name(self, name): self.__name = name

    def set_time(self, time): self.__time = time

    def set_level(self, level): self.level = level

    def save_data_player(self):
        insert_player(self.__name, self.__time, self.level)

    def __del__(self): pass
