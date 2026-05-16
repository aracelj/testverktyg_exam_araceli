from behave import given, when, then
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

url = "https://tap-ht25-testverktyg.github.io/exam/"

@given('the user is on the homepage')
def step_open_homepage(context):
    context.page.goto(url)

@when('the user clicks the "My Books" tab')
def step_mybook(context):
    context.page.locator(f'[data-testid="favorites"]').click()

@then('the user should see their list of favorite books')
def step_see_favorites_list(context):
    favorites_list = context.page.get_by_test_id("favorites-list")

    # Check that the list is visible
    expect(favorites_list).to_be_visible()

    # Optional: ensure it contains at least one item
    favorite_items = favorites_list.locator("[data-testid^='favorite-book']")
    expect(favorite_items.first).to_be_visible()
