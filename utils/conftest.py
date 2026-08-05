import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            slow_mo=500
        )

        page = browser.new_page()

        yield page

        browser.close()

# Hook that runs after every test
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = getattr(item, "page", None)

        if page:

            os.makedirs("screenshots", exist_ok=True)

            screenshot_name = f"screenshots/{item.name}.png"

            page.screenshot(
                path=screenshot_name,
                full_page=True
            )

            print(f"\nScreenshot saved: {screenshot_name}")