import pytest
from src.backend.booklist import BookStore, FavoriteBooks

# =========================
# UNIT TESTS (BookStore)
# =========================
@pytest.fixture
def store():
    return BookStore()

def test_initial_books_exist(store):
    assert len(store.books) == 13  # 13 books by default

def test_addBook__success(store):
    book = store.addBook("Python from scratch", "Jan Skansholm")
    initial_count = len(store.books)

    # checking added book
    assert book["title"] == "Python from scratch"
    assert book["author"] == "Jan Skansholm"
    assert book["favorite"] is False

    # checking id no.
    assert book["id"] == 14

    # checking if added to the catalog
    assert len(store.books) == 14

def test_addBook__duplicate():
    store = BookStore()

    # duplicate entry
    result = store.addBook("Snakes on a Plane: A Python Story", "Guido van Rossum")
    assert result is None

    # only one book added
    assert len(store.books) == 13

def test_get_book__id_found(store):
    store = BookStore()
    book = store.get_book(1)

    assert book is not None
    assert book["id"] == 1

def test_get_book__id_not_found():
    store = BookStore()
    book = store.get_book(100)

    assert book is None

def test_toggleFavorite__off():
    store = BookStore()

    store.toggleFavorite(1)  # On
    book = store.toggleFavorite(1)  # Off

    assert book["favorite"] is False
    assert store.click_count[1] == 2


def test_toggleFavorite__on():
    store = BookStore()

    book = store.toggleFavorite(1)

    assert book["favorite"] is True
    assert store.click_count[1] == 1

# =========================
# UNIT TESTS (FavoriteBooks)
# =========================
def test_add_book_favorite():
    fb = FavoriteBooks()

    book = {"id": 1, "title": "Snakes on a Plane: A Python Story"}
    fb.add_book_favorite(book)

    assert book in fb.favorite_books
    assert fb.stats["total_favorites"] == 1

def test_remove_book_favorite__existing():
    fb = FavoriteBooks()

    book = {"id": 1, "title": "Snakes on a Plane: A Python Story"}
    fb.add_book_favorite(book)
    fb.remove_book_favorite(book)

    assert book not in fb.favorite_books
    assert fb.stats["total_favorites"] == 0

def test_remove_book_favorite__non_existing():
    fb = FavoriteBooks()

    book = {"id": 1, "title": "Snakes on a Plane: A Python Story"}
    fb.remove_book_favorite(book)

    assert fb.stats["total_favorites"] == 0
    assert len(fb.favorite_books) == 0

def test_get_favorites():
    fb = FavoriteBooks()

    book1 = {"id": 1, "title": "Snakes on a Plane: A Python Story"}
    book2 = {"id": 2, "title": "The Pragmatic Procrastinato"}

    fb.add_book_favorite(book1)
    fb.add_book_favorite(book2)

    result = fb.get_favorites()

    assert result == [book1, book2]

def test_get_stats():
    fb = FavoriteBooks()

    book = {"id": 1, "title": "Snakes on a Plane: A Python Story"}
    fb.add_book_favorite(book)
    stats = fb.get_stats()

    assert stats["total_favorites"] == 1

def test_get_stats_message():
    fb = FavoriteBooks()

    book = {"id": 1, "title": "Snakes on a Plane: A Python Story"}
    fb.add_book_favorite(book)
    message = fb.get_stats_message(13)

    expected = """Welcome!
    The list has 13 books.

    Our users have hearted 1 books."""

    assert message == expected