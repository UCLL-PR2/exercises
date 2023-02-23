class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'{self.title} written by {self.author}'

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r})"


book = Book('Atlas', 'Rand')
print(str(book))
print(repr(book))