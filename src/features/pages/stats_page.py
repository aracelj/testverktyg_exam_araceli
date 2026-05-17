import re
from playwright.sync_api import expect


class StatsPage:

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.get_by_test_id("statistics").click()

    def stars_count(self):
        return self.page.locator('[data-testid="stars-count"]')

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