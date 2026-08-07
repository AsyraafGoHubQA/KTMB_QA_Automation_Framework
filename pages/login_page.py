from pathlib import Path
from datetime import datetime

from playwright.sync_api import expect

from pages.base_page import BasePage


class LoginPage(BasePage):

    """
    ============================================================
    KTMB QA Framework v1.2
    Login Page Object
    ============================================================
    """

    # ============================================================
    # URL
    # ============================================================

    LOGIN_URL = (
        "https://ktmb-dev-online-web.nssit.com.my/Account/Login"
    )

    # ============================================================
    # Locators
    # ============================================================

    EMAIL = 'input[type="email"]'
    PASSWORD = 'input[type="password"]'
    LOGIN_BUTTON = 'button[type="submit"]'

    # ============================================================
    # Messages
    # ============================================================

    INVALID_CREDENTIAL = (
        "Incorrect email or password."
    )

    MULTIPLE_LOGIN = (
        "Not allow multiple login."
    )

    # ============================================================
    # Constructor
    # ============================================================

    def __init__(self, page):

        super().__init__(page)

    # ============================================================
    # Open Login Page
    # ============================================================

    def open_login(self):

        print("\nOpening Login Page...")

        self.navigate(
            self.LOGIN_URL
        )

        self.page.wait_for_load_state(
            "networkidle"
        )

        print("Login Page Loaded Successfully")

    # ============================================================
    # Fill Field
    # ============================================================

    def fill_if_not_empty(
        self,
        locator,
        value,
        field_name
    ):

        if value is None:

            print(f"{field_name}: None")

            return

        if str(value).strip() == "":

            print(f"{field_name}: Blank")

            return

        print(f"Entering {field_name}")

        self.fill(
            locator,
            str(value)
        )

    # ============================================================
    # Login
    # ============================================================

    def login(
        self,
        username,
        password
    ):

        print("\n========== LOGIN ==========")

        self.fill_if_not_empty(
            self.EMAIL,
            username,
            "Username"
        )

        self.fill_if_not_empty(
            self.PASSWORD,
            password,
            "Password"
        )

        print("Click Login Button")

        self.click(
            self.LOGIN_BUTTON
        )

        self.page.wait_for_timeout(
            1000
        )

    # ============================================================
    # Verify Login Success
    # ============================================================

    def verify_login_success(self):

        print("\nVerifying Login Success...")

        self.page.wait_for_load_state(
            "networkidle"
        )

        expect(self.page).not_to_have_url(
            "**/Account/Login"
        )

        print("Login Successful")    
    
    # ============================================================
    # Verify Failure
    # ============================================================

    def verify_failure(self, validation):

        print("\n========== VERIFY FAILURE ==========")

        validation = str(validation).strip().lower()

        print(f"Validation : {validation}")

        # --------------------------------------------------------
        # Invalid Credential
        # --------------------------------------------------------

        if validation == "invalid_credential":

            expect(
                self.page.locator(
                    f"text={self.INVALID_CREDENTIAL}"
                )
            ).to_be_visible()

            print("Invalid Credential Validation Passed")

        # --------------------------------------------------------
        # Invalid Email Format
        # --------------------------------------------------------

        elif validation == "invalid_email_format":

            expect(self.page).to_have_url(
                self.LOGIN_URL
            )

            email_value = self.page.locator(
                self.EMAIL
            ).input_value()

            assert email_value != ""

            print("Invalid Email Format Validation Passed")

        # --------------------------------------------------------
        # Empty Username
        # --------------------------------------------------------

        elif validation == "empty_username":

            expect(self.page).to_have_url(
                self.LOGIN_URL
            )

            username = self.page.locator(
                self.EMAIL
            ).input_value()

            assert username == ""

            print("Empty Username Validation Passed")

        # --------------------------------------------------------
        # Empty Password
        # --------------------------------------------------------

        elif validation == "empty_password":

            expect(self.page).to_have_url(
                self.LOGIN_URL
            )

            password = self.page.locator(
                self.PASSWORD
            ).input_value()

            assert password == ""

            print("Empty Password Validation Passed")

        # --------------------------------------------------------
        # Multiple Login
        # --------------------------------------------------------

        elif validation == "multiple_login":

            expect(
                self.page.locator(
                    f"text={self.MULTIPLE_LOGIN}"
                )
            ).to_be_visible()

            print("Multiple Login Validation Passed")

        # --------------------------------------------------------
        # Unknown Validation
        # --------------------------------------------------------

        else:

            raise Exception(
                f"Unknown Validation : {validation}"
            )

        print("Failure Validation Completed")    
    
    # ============================================================
    # Capture Success Screenshot
    # ============================================================

    def capture_success_screenshot(self, tc_id):

        folder = Path("screenshots/Passed")
        folder.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        screenshot = folder / f"{tc_id}_{timestamp}.png"

        self.page.screenshot(
            path=str(screenshot),
            full_page=True
        )

        print("\n==========================================")
        print("PASS Screenshot Captured")
        print(screenshot)
        print("==========================================")

        return str(screenshot)

    # ============================================================
    # Capture Failure Screenshot
    # ============================================================

    def capture_failure_screenshot(self, tc_id):

        folder = Path("screenshots/Failed")
        folder.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        screenshot = folder / f"{tc_id}_{timestamp}.png"

        self.page.screenshot(
            path=str(screenshot),
            full_page=True
        )

        print("\n==========================================")
        print("FAIL Screenshot Captured")
        print(screenshot)
        print("==========================================")

        return str(screenshot)

    # ============================================================
    # Wait
    # ============================================================

    def wait(self, milliseconds):

        self.page.wait_for_timeout(
            milliseconds
        )

    # ============================================================
    # Get Current URL
    # ============================================================

    def current_url(self):

        return self.page.url

    # ============================================================
    # Check Login Page
    # ============================================================

    def is_login_page(self):

        return "/Account/Login" in self.page.url    
    
    # ============================================================
    # Print Test Header
    # ============================================================

    def print_test_header(self, tc_id):

        print("\n")
        print("=" * 70)
        print(f"Executing Test Case : {tc_id}")
        print("=" * 70)

    # ============================================================
    # Print Test Footer
    # ============================================================

    def print_test_footer(self):

        print("=" * 70)
        print("Execution Completed")
        print("=" * 70)

    # ============================================================
    # Logout
    # ============================================================

    def logout(self):

        try:

            print("\nAttempting Logout...")

            logout_button = self.page.get_by_role(
                "link",
                name="Logout"
            )

            if logout_button.count() > 0:

                logout_button.click()

                self.page.wait_for_load_state(
                    "networkidle"
                )

                print("Logout Successful")

            else:

                print("Logout button not found.")

        except Exception as e:

            print(f"Logout skipped : {e}")

    # ============================================================
    # Generic Screenshot
    # ============================================================

    def take_screenshot(
        self,
        folder,
        file_name
    ):

        folder = Path(folder)

        folder.mkdir(
            parents=True,
            exist_ok=True
        )

        screenshot = folder / file_name

        self.page.screenshot(
            path=str(screenshot),
            full_page=True
        )

        print(f"Screenshot Saved : {screenshot}")

        return str(screenshot)

    # ============================================================
    # Pause (Debug Only)
    # ============================================================

    def pause(self):

        self.page.pause()    
    
    # ============================================================
    # Verify Failure Scenario
    # ============================================================

    def verify_failure(self, validation):

        print("\n========== VERIFY FAILURE ==========")

        validation = str(validation).strip().lower()

        print(f"Validation : {validation}")

        # ========================================================
        # Invalid Credential
        # ========================================================

        if validation == "invalid_credential":

            expect(
                self.page.locator(
                    f"text={self.INVALID_CREDENTIAL}"
                )
            ).to_be_visible()

            print("Invalid Credential Validation Passed")

        # ========================================================
        # Invalid Email Format
        # ========================================================

        elif validation == "invalid_email_format":

            expect(self.page).to_have_url(
                self.LOGIN_URL
            )

            print("Invalid Email Format Validation Passed")

        # ========================================================
        # Empty Username
        # ========================================================

        elif validation == "empty_username":

            expect(self.page).to_have_url(
                self.LOGIN_URL
            )

            print("Empty Username Validation Passed")

        # ========================================================
        # Empty Password
        # ========================================================

        elif validation == "empty_password":

            expect(self.page).to_have_url(
                self.LOGIN_URL
            )

            print("Empty Password Validation Passed")

        # ========================================================
        # Multiple Login
        # ========================================================

        elif validation == "multiple_login":

            expect(
                self.page.locator(
                    f"text={self.MULTIPLE_LOGIN}"
                )
            ).to_be_visible()

            print("Multiple Login Validation Passed")

        # ========================================================
        # Unknown Validation
        # ========================================================

        else:

            raise Exception(
                f"Unknown Validation : {validation}"
            )

        print("Failure Validation Completed")