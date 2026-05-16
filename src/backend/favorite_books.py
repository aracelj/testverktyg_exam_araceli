class FavoriteBooks:
    def __init__(self):
        self.books = []

    def add_favorite(self, book):
        if book not in self.books:
            self.books.append(book)

    def remove_favorite(self, book):
        if book in self.books:
            self.books.remove(book)