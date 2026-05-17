from playwright.sync_api import sync_playwright


def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(
        headless=True  # for CI pipeline
    )


def before_scenario(context, scenario):
    # NEW clean browser context per scenario (VERY IMPORTANT)
    context.browser_context = context.browser.new_context()
    context.page = context.browser_context.new_page()


def after_scenario(context, scenario):
    # Close everything after each test → prevents "cache state"
    context.browser_context.close()


def after_all(context):
    context.browser.close()
    context.playwright.stop()