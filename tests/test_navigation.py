from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_data.test_data import UserData
from locators.all_locators import (
    HomePageLocators,
    LoginPageLocators,
)

home_locators = HomePageLocators()
login_locators = LoginPageLocators()

class TestNavigation:
    def test_profile_navigation(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        driver.get("https://stellarburgers.nomoreparties.site/")

        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_button))
        login_account_button.click()

        user = UserData()
        email_data = user.email
        password_data = user.password

        login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))

        login_input.send_keys(email_data)
        password_input.send_keys(password_data)

        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()

        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()

        constructor_link = wait.until(EC.element_to_be_clickable(home_locators.constructor_link))
        constructor_link.click()

        assert "https://stellarburgers.nomoreparties.site/" in driver.current_url

    def test_profile_to_constructor_transition(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        driver.get("https://stellarburgers.nomoreparties.site/")

        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_button))
        login_account_button.click()

        user = UserData()
        email_data = user.email
        password_data = user.password

        login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))

        login_input.send_keys(email_data)
        password_input.send_keys(password_data)

        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()

        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()

        wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))
        assert "https://stellarburgers.nomoreparties.site/account/profile" in driver.current_url

    def test_profile_to_constructor_via_logo(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        driver.get("https://stellarburgers.nomoreparties.site/")

        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_button))
        login_account_button.click()

        user = UserData()
        email_data = user.email
        password_data = user.password

        login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))

        login_input.send_keys(email_data)
        password_input.send_keys(password_data)

        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()

        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()

        stellar_burgers_logo = wait.until(EC.element_to_be_clickable(home_locators.stellar_burgers_logo))
        stellar_burgers_logo.click()

        assert "https://stellarburgers.nomoreparties.site/" in driver.current_url
