from playwright.sync_api import expect

class AddBookPage:

    def __init__(self, page):
        self.page = page

        # tabs / buttons
        self.add_book_tab = page.get_by_test_id("add-book")

        # form fields (appear after clicking tab)
        self.title_input = page.get_by_test_id("add-input-title")
        self.author_input = page.get_by_test_id("add-input-author")
        self.submit_button = page.get_by_test_id("add-submit")

        # catalog tab (for verification)
        self.catalog_tab = page.get_by_test_id("catalog")

    # STEP 1: open homepage
    def open_homepage(self):
        self.page.wait_for_load_state("domcontentloaded")

    # STEP 2: open Add Book section
    def open_add_book(self):
        self.add_book_tab.wait_for(state="visible")
        self.add_book_tab.click()

        # wait for form to be ready
        self.title_input.wait_for(state="visible")

    # STEP 3: actions
    def enter_title(self, title: str):
        self.title_input.fill(title)

    def enter_author(self, author: str):
        self.author_input.fill(author)

    def submit(self):
        self.submit_button.click()

    def expect_book_added(self, title: str, author: str):
        book = self.page.locator(f"text={title}").first

        expect(book).to_be_visible()
        expect(self.page.locator(f"text={author}")).to_be_visible()


