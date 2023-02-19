class CircularBuffer:
    def __init__(self, max_size):
        self.__size = 0
        self.__insertion_index = 0
        self.__items = [None] * max_size

    def add(self, item):
        self.__items[self.__insertion_index] = item
        self.__insertion_index = (self.__insertion_index + 1) % len(self.__items)
        self.__size = min(len(self.__items), self.__size + 1)

    def __getitem__(self, index):
        if self.__size < len(self.__items):
            return self.__items[index]
        else:
            return self.__items[(index + self.__insertion_index) % len(self.__items)]

    def __len__(self):
        return self.__size
