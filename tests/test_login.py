import os
import pytest

from pages.login_page import LoginPage
from utils.excel_reader import read_login_data


# ==========================================================
# Read Test Data
# ==========================================================

selected_tc = os.getenv("SELECTED_TC")

if selected_tc:

    print(f"\nRunning Selected Test Case : {selected_tc}")

    test_data = read_login_data(
        "data/LoginData.xlsx",
        selected_tc
    )

else:

    print("\nRunning Full Regression Suite")

    test_data = read_login_data(
        "data/LoginData.xlsx"
    )


# ==========================================================
# Execute Normal Login
# ==========================================================

def execute_normal_login(page, test_case):

    login = LoginPage(page)

    tc_id = test_case["tc"]
    username = test_case["username"]
    password = test_case["password"]
    expected = test_case["expected"]
    validation = test_case["validation"]

    login.print_test_header(tc_id)

    print(f"Username   : {username}")
    print(f"Expected   : {expected}")
    print(f"Validation : {validation}")

    login.open_login()

    login.login(
        username,
        password
    )    
    
    # ======================================================
    # Success Scenario
    # ======================================================

    if expected.lower() == "success":

        login.verify_login_success()

        login.capture_success_screenshot(
            tc_id
        )

    # ======================================================
    # Failure Scenario
    # ======================================================

    else:

        login.verify_failure(
            validation
        )

        login.capture_failure_screenshot(
            tc_id
        )

    login.wait(2000)

    login.print_test_footer()


# ==========================================================
# Execute Multiple Login (TC006)
# ==========================================================

def execute_multiple_login(browser, test_case):

    tc_id = test_case["tc"]
    username = test_case["username"]
    password = test_case["password"]

    print("\n")
    print("=" * 70)
    print(f"Executing Test Case : {tc_id}")
    print("=" * 70)

    # ---------------------------------------------
    # Browser Context 1
    # ---------------------------------------------

    context1 = browser.new_context()

    page1 = context1.new_page()

    login1 = LoginPage(page1)

    login1.open_login()

    login1.login(
        username,
        password
    )

    login1.verify_login_success()

    print("First Login Successful")

    # ---------------------------------------------
    # Browser Context 2
    # ---------------------------------------------

    context2 = browser.new_context()

    page2 = context2.new_page()

    login2 = LoginPage(page2)

    login2.open_login()

    login2.login(
        username,
        password
    )

    login2.verify_failure(
        "multiple_login"
    )

    login2.capture_success_screenshot(
        tc_id
    )

    print("Multiple Login Validation Passed")

    context2.close()
    context1.close()

    print("=" * 70)
    print("Execution Completed")
    print("=" * 70)

# ==========================================================
# Execute Test Cases
# ==========================================================

@pytest.mark.parametrize(
    "test_case",
    test_data,
    ids=[row["tc"] for row in test_data]
)
def test_login(page, browser, test_case):

    tc_id = test_case["tc"]
    validation = str(test_case["validation"]).strip().lower()

    try:

        # ======================================================
        # TC006 - Multiple Login
        # ======================================================

        if validation == "multiple_login":

            execute_multiple_login(
                browser,
                test_case
            )

        # ======================================================
        # Normal Login Flow
        # ======================================================

        else:

            execute_normal_login(
                page,
                test_case
            )

        print(f"\n✅ {tc_id} PASSED")

    except Exception as e:

        print(f"\n❌ {tc_id} FAILED")

        print(str(e))

        try:

            login = LoginPage(page)

            login.capture_failure_screenshot(
                tc_id
            )

        except Exception:

            pass

        raise

    finally:

        print("\n")
        print("=" * 70)
        print("End of Test Case")
        print("=" * 70)