import re
from playwright.sync_api import expect


class StatsPage:

    def __init__(self, page):
        self.page = page
        self.book_count = page.get_by_test_id("book-count")
        self.favorite_count = page.get_by_test_id("stars-count")
        self.statistics_tab = page.get_by_test_id("statistics")

    def open(self):
        self.page.get_by_test_id("statistics").click()

    def stars_count(self):
        return self.page.locator('[data-testid="stars-count"]')

    def books_count(self):
        return self.page.locator('[data-testid="books-count"]')

    def get_count(self):
        text = self.page.locator('[data-testid="stars-count"]').inner_text()

        match = re.search(r"\d+", text)
        return int(match.group()) if match else 0

    def expect_count_increased(self, previous):
        current = self.get_count()
        assert current == previous + 1

    def expect_count_decreased(self, previous_count):
        current = self.get_count()

        assert current == previous_count - 1

    def open_statistics(self):
        self.statistics_tab.wait_for(state="visible")
        self.statistics_tab.click()

    def expect_statistics_visible(self):
        expect(self.book_count).to_be_visible()
        expect(self.favorite_count).to_be_visible()

    def expect_total_books(self, expected: str):
        expect(self.book_count).to_contain_text(expected)

    def expect_favorite_books(self, expected):

        expect(self.favorite_count).to_contain_text(expected)