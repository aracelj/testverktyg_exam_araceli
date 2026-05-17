from behave import given, when, then
from src.features.pages.catalog_page import CatalogPage
from src.features.pages.stats_page import StatsPage


@given('the user is on the homepage')
def step_homepage(context):

    context.catalog = CatalogPage(context.page)
    context.stats = StatsPage(context.page)

    context.catalog.open()


@when('the user opens the "Statistics" section')
def step_click_statistics(context):
    context.stats.open_statistics()

    context.stats.expect_statistics_visible()


@then('the total number of books in the catalog should be "{total_books}"')
def step_page_displayed(context, total_books):

    context.stats.expect_total_books(total_books)

@then('the total number of favorite books should be "{total_fav_books}"')
def step_favorites_visible(context, total_fav_books):

    context.stats.expect_favorite_books(total_fav_books)