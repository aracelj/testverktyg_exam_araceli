from behave import given, when, then
from playwright.sync_api import sync_playwright


url = "https://tap-ht25-testverktyg.github.io/exam/"

""" Mark book as favorite """
@given('the user is viewing the homepage')
def step_open_homepage(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True)
    context.page = context.browser.new_page()

    context.page.goto(url)

@when('the user clicks the heart icon next to a book titled "{title}"')
def step_click_heart(context, title):
    context.page.locator(f'[data-testid="star-{title}"]').click()

@then('the book should be marked as favorite')
def step_book_marked_as_favorite(context):
    star = context.page.locator('[data-testid^="star-The Pragmatic Procrastinator"]').first

    # checks real state change
    assert "selected" in star.get_attribute("class")

@then('the selected book should display a heart icon next to the title "{title}"')
def step_favorite_icon_visible(context, title):
    star = context.page.locator(f'[data-testid="star-{title}"]')

    # ensures element exists
    assert start.count() == 1

    # ensures it is visually marked as favorite
    assert "selected" in star.get_attribute("class")



