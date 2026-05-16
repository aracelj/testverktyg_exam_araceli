import pytest
from src.backend.booklist import BookStore


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
    initial_count = len(store.books)

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

    store.toggleFavorite(1)  # ON
    book = store.toggleFavorite(1)  # OFF

    assert book["favorite"] is False
    assert store.click_count[1] == 2


def test_toggleFavorite__on():
    store = BookStore()

    book = store.toggleFavorite(1)

    assert book["favorite"] is True
    assert store.click_count[1] == 1

