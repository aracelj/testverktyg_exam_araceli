import re
from behave import given, when, then
from playwright.sync_api import sync_playwright

url = "https://tap-ht25-testverktyg.github.io/exam/"


# ----------------------------
# SETUP + MARK FAVORITE
# ----------------------------
@given('the book "{title}" is marked as favorite')
def step_mark_favorite(context, title):

    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()

    context.page.set_default_timeout(5000)
    context.page.goto(url)

    context.page.locator(f'[data-testid="star-{title}"]').click()


# ----------------------------
# STATS CHECK (given state)
# ----------------------------
@given(u'the statistics show {expected_count:d} favorite book')
def step_stats_initial(context, expected_count):

    text = context.page.locator('[data-testid="stars-count"]').inner_text()
    actual_count = int(re.search(r"\d+", text).group())

    assert actual_count == expected_count, (
        f"Expected {expected_count}, got {actual_count}"
    )


# ----------------------------
# CLICK HEART TWICE
# ----------------------------
@when(u'the user clicks the heart icon for "{title}" {times:d} times')
def step_click_twice(context, title, times):

    locator = context.page.locator(f'[data-testid="star-{title}"]')

    for _ in range(times):
        locator.click()

# ----------------------------
# VERIFY FAVORITE STATE
# ----------------------------
@then(u'the book "{title}" should be marked as favorite')
def step_is_favorite(context, title):

    star = context.page.locator(f'[data-testid="star-{title}"]')
    class_attr = star.get_attribute("class") or ""

    assert "selected" in class_attr


@then(u'the book "{title}" should no longer be marked as favorite')
def step_not_favorite(context, title):

    star = context.page.locator(f'[data-testid="star-{title}"]')
    class_attr = star.get_attribute("class") or ""

    assert "selected" not in class_attr


# ----------------------------
# REMOVE FROM LIST
# ----------------------------
@then(u'the book "{title}" should be removed from the favorites list')
def step_removed(context, title):

    assert context.page.locator(f'text={title}').count() == 0


# ----------------------------
# STATS CHECK AFTER ACTIONS
# ----------------------------
@then(u'the statistics should show {expected_count:d} favorite books')
def step_stats_final(context, expected_count):

    text = context.page.locator('[data-testid="stars-count"]').inner_text()
    actual_count = int(re.search(r"\d+", text).group())

    assert actual_count == expected_count, (
        f"Expected {expected_count}, got {actual_count}. Full text: {text}"
    )


# ----------------------------
# TOGGLE LOGIC CHECK (IMPORTANT)
# ----------------------------
@then(u'the book "{title}" should be {"favorite" if True else "not favorite"} after {times:d} clicks')
def step_toggle_state(context, title, times):

    star = context.page.locator(f'[data-testid="star-{title}"]')
    class_attr = star.get_attribute("class") or ""

    is_favorite = "selected" in class_attr
    expected = (times % 2 == 1)

    assert is_favorite == expected, (
        f"After {times} clicks expected favorite={expected}, got {is_favorite}"
    )

