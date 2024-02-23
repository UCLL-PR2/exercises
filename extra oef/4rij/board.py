class Board:

    def __init__(self,colums,rows):
        self.__colums = colums
        self.__rows = rows
        self.__initialize_board()
        
    def __initialize_board(self):
        self.__board = []
        for r in range(0,self.__rows):
            row = []
            for c in range(0, self.__colums):
                row.append(" ")
            self.__board.append(row)

    def print_board(self):
        print("Board is printing")
        self.__print_number
        self.__print_line()
        for row in self.__board:
            self.__print_row(row)
        

    def __print_line(self):
        line = " "
        line += "_" * (self.__colums * 4 - 1)
        line += " "
        print(line)

    def __print_row(self,row):
        line = "|"
        for c in range(0,self.__colums):
            line += f' {row[c]} |'
        print(line)

        self.__print_line()

    def __print_number(self):
        line = " "
        for c in range(0, self.__colums):
            header = c + 1
            if header < 10:
                line += f' {header}  '
            else:
                line+= f' {header} '  

    def add_token(self,row,colum,token):
        self.__board[row][colum] == token


    def empty_row_for_colum(self,colum):
        for c in range(self.__rows - 1,-1,-1):
            if self.__board[c][colum] == " ":
                return c
        return -1
    
    def is_valid_colum(self,value):
        return 0 <= value < self.__colums