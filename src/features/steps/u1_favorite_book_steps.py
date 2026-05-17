from behave import given, when, then
from pages.catalog_page import CatalogPage
import re
from playwright.sync_api import expect

# [U1] As a user, I want to be able to click the toggle icon beside a book in the catalog so that I can mark it as favorite.
@given('a book "{title}" is not marked as favorite')
def step_not_favorite(context, title):

    context.catalog = CatalogPage(context.page)
    context.catalog.open()

    favorite = context.catalog.star_button(title)

    # ensure clean state (unselected)
    if "selected" in (favorite.get_attribute("class") or ""):
        favorite.click()

    expect(favorite).not_to_have_class(re.compile(".*selected.*"))


@when('the user clicks the toggle icon for the book "{title}"')
def step_click_toggle(context, title):

    context.catalog.click_favorite(title)


@then('the book "{title}" is marked as favorite')
def step_marked(context, title):

    context.catalog.expect_book_marked(title)

