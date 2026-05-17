import pytest
from src.backend.booklist import BookStore, FavoriteBooks


@pytest.fixture
def store():
    return BookStore()

# =========================
# 1. ADD → FAVORITE → UNFAVORITE (FULL CYCLE)
# =========================
def test_favorite_unfavorite_cycle():
    store = BookStore()

    book = store.addBook("Python from scratch", "Jan Skansholm")

    # favorite
    store.toggleFavorite(book["id"])
    assert book in store.favorite_manager.favorite_books
    assert store.favorite_manager.stats["total_favorites"] == 1

    # unfavorite
    store.toggleFavorite(book["id"])
    assert book not in store.favorite_manager.favorite_books
    assert store.favorite_manager.stats["total_favorites"] == 0

    print("test_favorite_unfavorite_cycle PASSED")

# =========================
# 2. MULTIPLE BOOKS + PARTIAL UNFAVORITE
# =========================
def test_partial_favorites():
    store = BookStore()

    book1 = store.addBook("Learning Python", "Mark Lutz")
    book2 = store.addBook("Automate the Boring Stuff with Python", "Al Sweigart")
    book3 = store.addBook("Effective Python", "Brett Slatkin")

    store.toggleFavorite(book1["id"])
    store.toggleFavorite(book2["id"])
    store.toggleFavorite(book3["id"])

    # remove one
    store.toggleFavorite(book2["id"])

    assert book1 in store.favorite_manager.favorite_books
    assert book2 not in store.favorite_manager.favorite_books
    assert book3 in store.favorite_manager.favorite_books

    assert store.favorite_manager.stats["total_favorites"] == 2

    print("test_partial_favorites PASSED")

# =========================
# 3. CATALOG INTEGRATION TEST
# =========================
def test_catalog_independent_of_favorites():
    store = BookStore()

    book = store.addBook("Python from scratch", "Jan Skansholm")

    store.toggleFavorite(book["id"])

    # catalog must still contain book
    assert book in store.books

    # favorites must also contain book
    assert book in store.favorite_manager.favorite_books

    print("test_catalog_independent_of_favorites PASSED")


# =========================
# 4. STATISTICS ACCURACY TEST
# =========================
def test_statistics_accuracy():
    store = BookStore()

    book1 = store.addBook("Python from scratc", "Jan Skansholm")
    book2 = store.addBook("Python Crash Course", "Eric Matthes")

    store.toggleFavorite(book1["id"])
    store.toggleFavorite(book2["id"])
    store.toggleFavorite(book1["id"])  # remove

    assert store.favorite_manager.stats["total_favorites"] == 1

    print("test_statistics_accuracy PASSED")


# =========================
# 5. REPEATED TOGGLE (UI SIMULATION)
# =========================
def test_repeated_toggle_behavior():
    store = BookStore()

    book = store.addBook("Learning Python", "Mark Lutz")

    for _ in range(10):
        store.toggleFavorite(book["id"])

    # even number of clicks → not favorite
    assert book not in store.favorite_manager.favorite_books
    assert store.favorite_manager.stats["total_favorites"] == 0

    print("test_repeated_toggle_behavior PASSED")
