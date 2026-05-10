class FavoriteBooks:
    def __init__(self):
        self.books = []

    def add(self, book):
        if book not in self.books:
            self.books.append(book)

    def remove(self, book):
        if book in self.books:
            self.books.remove(book)