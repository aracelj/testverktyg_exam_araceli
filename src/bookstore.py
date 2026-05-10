class BookStore:
    def __init__(self):
        self.books = []
        self.next_id = 1

    def addBook(self, author, title):
        book = {
            "id": self.next_id,
            "author": author,
            "title": title,
            "favorite": False
        }
        self.books.append(book)
        self.next_id += 1
        return book

    def toggleFavorite(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                book["favorite"] = not book["favorite"]
                return book

        return None