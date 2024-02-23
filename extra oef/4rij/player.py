class Player:
    def __init__(self, name , token):
        self.name = name
        self.token = token

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def token(self):
        return self.__token
    
    @token.setter
    def token(self,value):
        self.__token = value

    def __str__(self):
        return f'Player {self.name} will play with token {self.token}'


