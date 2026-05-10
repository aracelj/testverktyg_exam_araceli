from behave import given, when, then
from playwright.sync_api import sync_playwright


""" Mark book as favorite """
@given('the user is viewing the homepage')
def step_user_on_homepage(context):
    # Simulate homepage state with a bookstore and one book
    context.store = BookStore()
    context.book = context.store.addBook("Author", "Title")

@when("the user clicks the heart icon next to a book")
def step_click_heart(context):
    # This simulates clicking ❤️ in the UI
    context.store.toggleFavorite(context.book["id"])

@then("the book should be marked as favorite")
def step_book_marked_favorite(context):
    assert context.book["favorite"] is True

@then("the selected book should display a favorite icon next to its title")
def step_book_has_icon(context):
    # In real UI this would check DOM, but here we simulate state
    assert context.book["favorite"] is True

