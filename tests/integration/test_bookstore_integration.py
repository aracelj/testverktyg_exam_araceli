from src.bookstore import BookStore


def test_add_book_and_toggle_favorite_flow():
    store = BookStore()

    # Step 1: add a book (like user clicking "Add")
    book = store.addBook("John Grisham", "The Pelican Brief")

    # Step 2: toggle favorite (like clicking ❤️ button)
    store.toggleFavorite(book["id"])

    # Step 3: check final state
    assert book["favorite"] is True
    assert book["id"] == 1
    assert book["author"] == "John Grisham"
    assert book["title"] == "The Pelican Brief"