""" Remove a favorite book """
@given('the book "{title}" is marked as favorite')
def step_book_marked_favorite(context, title):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True)
    context.page = context.browser.new_page()

    context.page.goto("https://tap-ht25-testverktyg.github.io/exam/")

    # click heart icon for first book (simplified selector example)
    context.page.locator(".heart-icon").first.click()

    context.book_title = title