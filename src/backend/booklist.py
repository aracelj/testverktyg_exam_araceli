class BookStore:

    def __init__(self):
        self.favorite_manager = FavoriteBooks()
        self.click_count = {}

        """ 13 default books"""
        self.books = [
            {"id": 1, "title": "Snakes on a Plane: A Python Story", "author": "Guido van Rossum", "favorite": False},
            {"id": 2, "title": "The Pragmatic Procrastinator", "author": "Dave Thomasson", "favorite": False},
            {"id": 3, "title": "Python for People Who Hate Snakes", "author": "Monty Pythonsson", "favorite": False},
            {"id": 4, "title": "Why Your Tests Are Lying to You", "author": "Kent Backdoor", "favorite": False},
            {"id": 5, "title": "Playwright: Click It Till You Make It", "author": "Microslop Browserdóttir", "favorite": False},
            {"id": 6, "title": "Git Blame and Other Ways to Lose Friends", "author": "Linus Torvalds", "favorite": False},
            {"id": 7, "title": "Learn Python in 21 Years", "author": "Sams Teachyourself", "favorite": False},
            {"id": 8, "title": "Agile Is a Feeling", "author": "Jeff Sutherland", "favorite": False},
            {"id": 9, "title": "Playwright: Waiting for Selectors", "author": "Samuel Barclay Beckett", "favorite": False},
            {"id": 10, "title": "Stack Overflow: A Love Storyt", "author": "Copy Pasta", "favorite": False},
            {"id": 11, "title": "My First Regex (And Last)", "author": "Larry Wallström", "favorite": False},
            {"id": 12, "title": "The Developer Who Knew Nothing", "author": "George R.R. Martin", "favorite": False},
            {"id": 13, "title": "The Bugs are Coming", "author": "George R.R. Martin", "favorite": False},
        ]

    def addBook(self, title, author):
        # checking if book to add already exist
        for book in self.books:
            if book["title"] == title and book["author"] == author:
                return None

        book = {
            "id": len(self.books) + 1,
            "title": title,
            "author": author,
            "favorite": False
        }

        self.books.append(book)
        return book

    def get_book(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                return book
        return None

    def toggleFavorite(self, book_id):
        book = self.get_book(book_id)

        if not book:
            return None

        # count clicks
        self.click_count[book_id] = self.click_count.get(book_id, 0) + 1
        clicks = self.click_count[book_id]

        # odd clicks → ON
        if clicks % 2 == 1:
            book["favorite"] = True
            self.favorite_manager.add_favorite(book)

        # even clicks → OFF
        else:
            book["favorite"] = False
            self.favorite_manager.remove_favorite(book)

        return book


class FavoriteBooks:

    def __init__(self):
        self.favorite_books = []
        self.stats = {
            "total_favorites": 0
        }

    def add_favorite(self, book):
        if book not in self.favorite_books:
            self.favorite_books.append(book)
            self.stats["total_favorites"] += 1

    def remove_favorite(self, book):
        if book in self.favorite_books:
            self.favorite_books.remove(book)
            self.stats["total_favorites"] -= 1

    def get_favorites(self):
        return self.favorite_books

    def get_stats(self):
        return self.stats

    def get_stats_message(self, total_books):

        return f"""Welcome!
    The list has {total_books} books.

    Our users have hearted {self.stats['total_favorites']} books."""
