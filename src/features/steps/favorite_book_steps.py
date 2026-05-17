from behave import given, when, then
from pages.catalog_page import CatalogPage


@given('a list of books is displayed from the homepage catalog list')
def step_open_catalog(context):

    context.catalog = CatalogPage(context.page)
    context.catalog.open()


@when('the user clicks the toggle icon on "{title}"')
def step_click_favorite(context, title):

    context.catalog.click_favorite(title)


@then('the book "{title}" is marked as favorite')
def step_book_marked(context, title):

    context.catalog.expect_book_marked(title)

