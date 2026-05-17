import re
from playwright.sync_api import expect



class CatalogPage:

    def __init__(self, page):
        self.page = page

    # -------------------------
    # Locators
    # -------------------------
    def star_button(self, title):
        return self.page.locator(f'[data-testid="star-{title}"]')

    def stars_count(self):
        return self.page.locator('[data-testid="stars-count"]')

    def favorite_item(self, title):
        return self.page.locator(f'[data-testid="fav-{title}"]')

    def is_favorite(self, title):
        return "selected" in (self.star_button(title).get_attribute("class") or "")


    # -------------------------
    # Actions
    # -------------------------
    def open(self):
        self.page.goto("https://tap-ht25-testverktyg.github.io/exam/")

    def click_favorite(self, title):
        self.star_button(title).click()

    # -------------------------
    # Reads / helpers
    # -------------------------
    def get_favorite_count(self):
        text = self.stars_count().inner_text()
        match = re.search(r"\d+", text)
        return int(match.group()) if match else 0

    # -------------------------
    # Assertions
    # -------------------------
    def expect_book_marked(self, title):
        expect(self.star_button(title)).to_have_class(re.compile(".*selected.*"))

    def expect_favorite_visible(self, title):
        expect(self.favorite_item(title)).to_be_visible()

    def expect_count_increased(self, previous_count):
        current = self.get_favorite_count()
        assert current == previous_count + 1

    def expect_unselected(self, title):
        expect(self.star_button(title)).to_have_class(re.compile("star"))