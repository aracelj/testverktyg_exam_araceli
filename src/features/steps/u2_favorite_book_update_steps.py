from behave import given, when, then
from pages.catalog_page import CatalogPage
from pages.mybooks_page import MyBooksPage
from pages.stats_page import StatsPage


@given('a book "{title}" is marked as favorite')
def step_marked(context, title):

    context.catalog = CatalogPage(context.page)
    context.catalog.open()

    context.stats = StatsPage(context.page)

    # ensure known state
    context.catalog.click_favorite(title)
    context.catalog.expect_book_marked(title)


@when('the user opens the My Books section')
def step_open_my_books(context):

    context.mybooks = MyBooksPage(context.page)
    context.mybooks.open_mybooks()


@then('the book "{title}" should be visible in the favorites list')
def step_my_books(context, title):

    context.mybooks.expect_book_visible(title)


@then('the favorite count in statistics is increased by 1')
def step_stats(context):

    context.stats.open()
    context.stats.expect_count_increased(context.stats.get_count() - 1)