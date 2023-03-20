class PadZip:
    def __init__(self, left, right, padding=None):
        self.__left = iter(left)
        self.__right = iter(right)
        self.__padding = padding

    def __iter__(self):
        return self

    def __next__(self):
        end_reached = 0

        try:
            left = next(self.__left)
        except StopIteration:
            left = self.__padding
            end_reached += 1

        try:
            right = next(self.__right)
        except StopIteration:
            right = self.__padding
            end_reached += 1

        if end_reached == 2:
            raise StopIteration()

        return (left, right)
