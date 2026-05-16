from src.backend.bookstore import BookStore
from src.backend.favorite_books import FavoriteBooks


def test_add_and_remove_favorite_flow():
    store = BookStore()
    favorites = FavoriteBooks()

    # Step 1: user adds a book
    book = store.addBook("John Grisham", "The Pelican Brief")

    # Step 2: user clicks ❤️ (add to favorites)
    store.toggleFavorite(book["id"])
    favorites.add(book)

    # Check it was added
    assert book in favorites.books
    assert book["favorite"] is True

    # Step 3: user unclicks ❤️ (remove from favorites)
    store.toggleFavorite(book["id"])
    favorites.remove(book)

    # Check it was removed
    assert book not in favorites.books
    assert book["favorite"] is False