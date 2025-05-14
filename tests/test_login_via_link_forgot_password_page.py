from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_data.test_data import UserData
from helpers.data_helpers import DataHelper
from locators.all_locators import (
    HomePageLocators,
    LoginPageLocators,
    RegistrationPageLocators,
    AccountPageLocators,
    ForgotPasswordLocators
)

home_locators = HomePageLocators()
login_locators = LoginPageLocators()
registration_locators = RegistrationPageLocators()
account_locators = AccountPageLocators()
forgot_password_locators = ForgotPasswordLocators()


class TestLogin:
    def test_login_forgot_password_page(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        sleep(3)

        login_link = wait.until(EC.element_to_be_clickable(forgot_password_locators.login_link))
        login_link.click()
        sleep(3)

        user = UserData()
        email_data = user.email
        password_data = user.password

        login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))

        login_input.send_keys(email_data)
        password_input.send_keys(password_data)

        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()
        sleep(3)

        assert "https://stellarburgers.nomoreparties.site/" in driver.current_url

        driver.quit()