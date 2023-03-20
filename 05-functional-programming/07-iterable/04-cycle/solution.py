class Cycle:
    def __init__(self, elts):
        self.__elts = list(elts)
        self.__index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__index = (self.__index + 1) % len(self.__elts)
        return self.__elts[self.__index]
