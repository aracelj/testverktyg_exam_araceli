from playwright.sync_api import sync_playwright

def before_scenario(context, scenario):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True)
    context.page = context.browser.new_page()

    context.page.set_default_timeout(5000)
    context.page.set_default_navigation_timeout(5000)

def after_scenario(context, scenario):
    if hasattr(context, "browser"):
        context.browser.close()

    if hasattr(context, "playwright"):
        context.playwright.stop()