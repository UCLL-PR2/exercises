class ChessPiece:
    def __init__(self, position, color):
        if not ChessPiece.is_valid_position(position):
            raise ValueError('invalid position')
        if not ChessPiece.is_valid_color(color):
            raise ValueError('invalid color')
        self.__position = position
        self.__color = color

    @property
    def position(self):
        return self.__position

    @property
    def color(self):
        return self.__color

    @staticmethod
    def is_valid_color(color):
        return color in ['black', 'white']

    @staticmethod
    def is_valid_position(position):
        return 0 <= position.x < 8 and 0 <= position.y < 8

    @staticmethod
    def keep_valid_positions(positions):
        return {pos for pos in positions if ChessPiece.is_valid_position(pos)}

    def move(self, new_position):
        if new_position not in self.legal_moves:
            raise ValueError("Invalid move")
        self.__position = new_position



class Pawn(ChessPiece):
    @property
    def legal_moves(self):
        direction = 1 if self.color == 'white' else -1
        return ChessPiece.keep_valid_positions({self.position.moved(0, direction)})


class King(ChessPiece):
    def legal_moves(self):
        return ChessPiece.keep_valid_positions(
            self.position.moved(dx, dy)
            for dx in [-1, 0, 1]
            for dy in [-1, 0, 1]
            if dx != 0 or dy != 0
        )
