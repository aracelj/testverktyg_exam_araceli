from src.favorite_books import FavoriteBooks


def test_add_favorite_book():
    favorites = FavoriteBooks()

    book = {
        "id": 1,
        "author": "Author",
        "title": "Title",
        "favorite": True
    }

    favorites.add(book)

    assert book in favorites.books


def test_remove_favorite_book():
    favorites = FavoriteBooks()

    book = {
        "id": 1,
        "author": "Author",
        "title": "Title",
        "favorite": True
    }

    favorites.add(book)
    favorites.remove(book)

    assert book not in favorites.books