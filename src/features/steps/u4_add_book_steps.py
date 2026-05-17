from behave import given, when, then

from pages.add_book_page import AddBookPage
from pages.catalog_page import CatalogPage
from pages.stats_page import StatsPage


@given('the user is on the catalog page')
def step_open_homepage(context):

    context.addbook = AddBookPage(context.page)
    context.catalog = CatalogPage(context.page)

    context.catalog.open()
    context.addbook.open_homepage()


@when('the user opens the "Add Book" section')
def step_open_add_book(context):

    context.addbook.open_add_book()


@when('the user enters a book with title "{title}" and author "{author}"')
def step_enter_book(context, title, author):

    context.addbook.enter_title(title)
    context.addbook.enter_author(author)


@when("the user submits the form")
def step_submit_form(context):

    context.addbook.submit()


@then('the book "{title}" by "{author}" should be added to the catalog list')
def step_verify_book_added(context, title, author):

    # optional: ensure catalog is visible first (safe sync)
    context.addbook.catalog_tab.click()

    # verify book exists in catalog
    context.addbook.expect_book_added(title, author)

