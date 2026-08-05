from pathlib import Path
from datetime import datetime

from pages.base_page import BasePage
from playwright.sync_api import expect


class LoginPage(BasePage):

    EMAIL = 'input[type="email"]'
    PASSWORD = 'input[type="password"]'
    LOGIN_BUTTON = 'button[type="submit"]'

    # -------------------------
    # Open Login Page
    # -------------------------
    def open_login(self):

        print("Opening Login Page...")

        self.navigate(
            "https://ktmb-dev-online-web.nssit.com.my/Account/Login"
        )

        self.page.wait_for_load_state("networkidle")

    # -------------------------
    # Fill textbox only if value exists
    # -------------------------
    def fill_if_not_empty(self, locator, value, field_name):

        if value is None or str(value).strip() == "":

            print(f"{field_name} is blank. Skip input.")

            return

        print(f"Entering {field_name}")

        self.fill(locator, str(value))

    # -------------------------
    # Login
    # -------------------------
    def login(self, username, password):

        print("\n========== Login Process ==========")

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

        self.click(self.LOGIN_BUTTON)

    # -------------------------
    # Success Validation
    # -------------------------
    def verify_login_success(self):

        print("Verifying Successful Login...")

        self.page.wait_for_load_state("networkidle")

        expect(self.page).not_to_have_url(
            "**/Account/Login"
        )

        print("Login Success Verified")

    # -------------------------
    # Failure Validation
    # -------------------------
    def verify_login_failed(self, tc_id):

        print("Verifying Login Failure...")

        # TC002 & TC003
        if tc_id in ["TC002", "TC003"]:

            expect(
                self.page.locator(
                    "text=Incorrect email or password."
                )
            ).to_be_visible()

        # TC004 - Empty Username
        elif tc_id == "TC004":

            expect(
                self.page.locator(self.EMAIL)
            ).to_be_focused()

        # TC005 - Empty Password
        elif tc_id == "TC005":

            expect(
                self.page.locator(self.PASSWORD)
            ).to_be_focused()

        print("Failure Validation Passed")

    # -------------------------
    # Close Popup
    # -------------------------
    def close_error_popup(self):

        ok_button = self.page.locator(
            "button:has-text('OK')"
        )

        if ok_button.count() > 0:

            print("Closing Error Popup")

            ok_button.click()

    # -------------------------
    # Success Screenshot
    # -------------------------
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

        print(f"✅ Success Screenshot saved:")
        print(screenshot)

        return str(screenshot)

    # -------------------------
    # Failure Screenshot
    # -------------------------
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

        print(f"❌ Failure Screenshot saved:")
        print(screenshot)

        return str(screenshot)