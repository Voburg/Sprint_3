from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_data.test_data import UserData
from helpers.data_helpers import DataHelper
from locators.all_locators import (
    HomePageLocators,
    LoginPageLocators,
    RegistrationPageLocators,
    AccountPageLocators
)

home_locators = HomePageLocators()
login_locators = LoginPageLocators()
registration_locators = RegistrationPageLocators()
account_locators = AccountPageLocators()


class TestVisitProfile:
    def test_visit_profile_via_account_link(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        driver.get("https://stellarburgers.nomoreparties.site/")
        sleep(3)

        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_button))
        login_account_button.click()
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

        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()
        sleep(3)

        stellar_burgers_logo = wait.until(EC.element_to_be_clickable(home_locators.stellar_burgers_logo))
        stellar_burgers_logo.click()
        sleep(3)

        assert "https://stellarburgers.nomoreparties.site/" in driver.current_url

        driver.quit()