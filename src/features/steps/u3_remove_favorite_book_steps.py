from behave import given, when, then
from pages.catalog_page import CatalogPage
from pages.mybooks_page import MyBooksPage
from pages.stats_page import StatsPage


@given('a book "{title}" is already marked as favorite')
def step_precondition(context, title):

    context.catalog = CatalogPage(context.page)
    context.mybooks = MyBooksPage(context.page)
    context.stats = StatsPage(context.page)

    context.catalog.open()

    # ensure book is favorited
    if not context.catalog.is_favorite(title):
        context.catalog.click_favorite(title)

    context.previous_count = context.stats.get_count()


@when('the user toggles the heart icon for the favorite book "{title}"')
def step_unfavorite(context, title):

    context.catalog.click_favorite(title)


@then('the book "{title}" is unmarked as favorite')
def step_unmarked(context, title):

    context.catalog.expect_unselected(title)

@then('the book "{title}" is removed from My Books list')
def step_removed_mybooks(context, title):
    context.mybooks.open_mybooks()
    context.mybooks.expect_not_visible(title)

@then('the favorite count in statistics is decreased by 1')
def step_stats(context):
    context.stats.open()

    expected_value = context.previous_count - 1

    actual_value = context.stats.get_count()

    assert actual_value == expected_value

