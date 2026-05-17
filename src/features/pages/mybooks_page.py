from playwright.sync_api import expect


class MyBooksPage:

    def __init__(self, page):
        self.page = page

        # UI elements
        self.favorites_container = page.get_by_test_id("favorites-list")

    def open_mybooks(self):
        self.page.get_by_test_id("favorites").click()

    def book_item(self, title):
        return self.page.locator(f'[data-testid="fav-{title}"]')

    def count(self):
        #return self.books().count()
        return self.page.locator('[data-testid^="fav-"]').count()

    def expect_book_visible(self, title):
        expect(self.book_item(title)).to_be_visible()

    def expect_not_visible(self, title):
        expect(self.book_item(title)).to_have_count(0)

    def expect_my_books_page_visible(self):
        # you can treat container as proof page is loaded
        expect(self.favorites_container).to_be_visible()

    def expect_favorites_visible(self):
        expect(self.favorites_container).to_be_visible()