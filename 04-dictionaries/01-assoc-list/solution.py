class AssocList:
    def __init__(self):
        self.__items = []

    def __setitem__(self, key, value):
        index = self.__find_key_index(key)
        if index == -1:
            self.__items.append([key, value])
        else:
            self.__items[index][1] = value

    def __contains__(self, key):
        return self.__find_key_index(key) != -1

    def __getitem__(self, key):
        index = self.__find_key_index(key)
        if index == -1:
            raise KeyError()
        else:
            return self.__items[index][1]

    def __len__(self):
        return len(self.__items)

    def __find_key_index(self, key):
        for i in range(len(self.__items)):
            k, v = self.__items[i]
            if k == key:
                return i
        return -1

    @property
    def keys(self):
        return [k for k, _ in self.__items]

    @property
    def values(self):
        return [v for _, v in self.__items]
