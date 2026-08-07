import os
import pytest


# ==========================================================
# Capture Screenshot on Failure
# ==========================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    page = item.funcargs.get("page")

    if page and report.failed:

        os.makedirs("screenshots", exist_ok=True)

        screenshot_path = f"screenshots/{item.name}.png"

        page.screenshot(
            path=screenshot_path,
            full_page=True
        )

        print(f"\nScreenshot saved: {screenshot_path}")