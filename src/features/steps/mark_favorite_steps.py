from behave import given, when, then
from playwright.sync_api import Page, expect


url = "https://tap-ht25-testverktyg.github.io/exam/"

""" 
# =========================
# GIVEN (open app)
# =========================
@given('a list of books is displayed from the homepage catalog list')
def step_open_catalog(context):
    context.page.goto(url)

# =========================
# WHEN (UI interaction)
# =========================
@when('the user clicks the toggle icon on "{title}"')
def step_click_heart(context, title):
    favorite = context.page.locator(
        '[data-testid="star-{title}"]'
    )

    favorite.click()

    assert "selected" in favorite.get_attribute("class")

@then('the book "{title}" should be added to the favorites list')
def step_check_favorites(context, title ):
    favorites = context.page.locator('[data-testid="{title}"]')
    assert favorites.count() >= 1

@then("the toggle icon should appear selected")
def step_heart_selected(context):
    assert "selected" in context.heart.get_attribute("class")

@then("the number of favorite books should increase by 1")
def step_stats(context):
    count = int(context.page.locator('[data-testid="favorite-count"]').inner_text())
    assert count >= 1
 """


#Mark book as favorite 
@given('the user is viewing the homepage')
def step_open_homepage(context):
    context.page.goto(url)

@when('the user clicks the heart icon next to a book titled "{title}"')
def step_click_heart(context, title):
    context.page.locator(f'[data-testid="star-{title}"]').click()

@then('the book should be marked as favorite')
def step_book_marked_as_favorite(context):
    star = context.page.locator('[data-testid^="star-The Pragmatic Procrastinator"]').first
    assert "selected" in (star.get_attribute("class") or "")

@then('the selected book should display a heart icon next to the title "{title}"')
def step_favorite_icon_visible(context, title):
    star = context.page.locator(f'[data-testid="star-{title}"]')
    assert star.count() == 1
    assert "selected" in (star.get_attribute("class") or "")