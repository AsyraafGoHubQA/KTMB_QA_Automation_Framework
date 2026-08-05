import os
import pytest

from pages.login_page import LoginPage
from utils.excel_reader import read_login_data

selected_tc = os.getenv("SELECTED_TC")

if selected_tc:
    test_data = read_login_data("data/LoginData.xlsx", selected_tc)
else:
    test_data = read_login_data("data/LoginData.xlsx")


@pytest.mark.parametrize(
    "test_case",
    test_data,
    ids=[row["tc"] for row in test_data]
)
def test_login(page, test_case):

    login = LoginPage(page)

    login.open_login()

    login.login(
        test_case["username"],
        test_case["password"]
    )

    if test_case["expected"] == "Success":

        login.verify_login_success()

        login.capture_success_screenshot(test_case["tc"])

        page.wait_for_timeout(10000)

    else:

        login.capture_failure_screenshot(test_case["tc"])

        login.verify_login_failed(test_case["tc"])

        page.wait_for_timeout(3000)

        login.close_error_popup()