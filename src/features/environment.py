from playwright.sync_api import sync_playwright

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True)


def before_scenario(context, scenario):
    context.context = context.browser.new_context()
    context.page = context.context.new_page()

    context.page.set_default_timeout(5000)
    context.page.set_default_navigation_timeout(5000)


def after_scenario(context, scenario):
    if hasattr(context, "context"):
        context.context.close()


def after_all(context):
    if hasattr(context, "browser"):
        context.browser.close()

    if hasattr(context, "playwright"):
        context.playwright.stop()



"""
import asyncio


def detect_runtime(label=""):
    try:
        loop = asyncio.get_running_loop()
        print(f"[{label}] ASYNC runtime detected:", loop)
    except RuntimeError:
        print(f"[{label}] SYNC runtime detected")

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
        context.playwright.stop()   """