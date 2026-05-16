from src.backend.bookstore import BookStore


def test_add_book():
    store = BookStore()
    book = store.addBook("Author", "Title")

    assert book["author"] == "Author"
    assert book["title"] == "Title"

def test_toggle_favorite():
    store = BookStore()
    book = store.addBook("Author", "Title")
    store.toggleFavorite(book["id"])

    assert book["favorite"] is True