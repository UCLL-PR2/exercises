from player import Player
from board import Board

class Game:
    def __init__(self):
        print("start spel")
        name_x = input("please input the name of player 1 who will play with x")
        p1 = Player(name_x , "X")
        name_o = input("please input the name of player 1 who will play with o")
        p2 = Player(name_o , "O")

        #print(p1)
        #print(p2)

        board = Board(7,6)
        board.print_board()

        won = False

        while not won:
            selection =input(f'Please select the number of the colum you want to drop a token into')
            if not selection.isnumeric():
                print("wrong selection. Please try again")
                continue

            colum = int(selection) - 1
            if not board.is_valid_colum(colum):
                print("Wrong colum. Please try again")
                continue

            row = board.empty_row_for_colum(colum)
            if row == -1:
                print("colum is full. Try again")
            board.add_token(row , colum , "X")
            board.print_board()



game1 = Game()