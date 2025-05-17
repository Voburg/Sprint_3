from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_data.test_data import UserData
from helpers.data_helpers import DataHelper

from locators.all_locators import (
    HomePageLocators,
    LoginPageLocators,
    RegistrationPageLocators,
    ForgotPasswordLocators,
    AccountPageLocators
)

home_locators = HomePageLocators()
login_locators = LoginPageLocators()
registration_locators = RegistrationPageLocators()
forgot_password_locators = ForgotPasswordLocators()
account_locators = AccountPageLocators()


class TestLogin:
    def test_login_button_main_page(self, create_driver):
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

        assert "https://stellarburgers.nomoreparties.site/" in driver.current_url

    def test_login_account_link(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        driver.get("https://stellarburgers.nomoreparties.site/")

        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()

        user = UserData()
        email_data = user.email
        password_data = user.password

        login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))

        login_input.send_keys(email_data)
        password_input.send_keys(password_data)

        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()

        assert "https://stellarburgers.nomoreparties.site/" in driver.current_url

    def test_login_forgot_password_page(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        login_link = wait.until(EC.element_to_be_clickable(forgot_password_locators.login_link))
        login_link.click()

        user = UserData()
        email_data = user.email
        password_data = user.password

        login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))

        login_input.send_keys(email_data)
        password_input.send_keys(password_data)

        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()

        assert "https://stellarburgers.nomoreparties.site/" in driver.current_url

    def test_login_registration_page(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        driver.get("https://stellarburgers.nomoreparties.site/register")

        login_link = wait.until(EC.element_to_be_clickable(registration_locators.login_link))
        login_link.click()

        user = UserData()
        email_data = user.email
        password_data = user.password

        login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))

        login_input.send_keys(email_data)
        password_input.send_keys(password_data)

        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()

        assert "https://stellarburgers.nomoreparties.site/" in driver.current_url

class TestLogout:
    def test_logout_via_button_profile_page(self, create_driver):
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

        logout_button = wait.until(EC.element_to_be_clickable(account_locators.logout_button))
        logout_button.click()

        wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

class TestRegistration:
    def test_register_new_user(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        driver.get("https://stellarburgers.nomoreparties.site/")

        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_button))
        login_account_button.click()

        registration_link = wait.until(EC.element_to_be_clickable(login_locators.registration_link))
        registration_link.click()

        name_data = DataHelper.generate_name()
        email_data = DataHelper.generate_login()
        password_data = DataHelper.generate_password()

        register_name_input = wait.until(EC.visibility_of_element_located(registration_locators.name_input))
        register_email_input = wait.until(EC.visibility_of_element_located(registration_locators.email_input))
        register_password_input = wait.until(EC.visibility_of_element_located(registration_locators.password_input))

        register_name_input.send_keys(name_data)
        register_email_input.send_keys(email_data)
        register_password_input.send_keys(password_data)

        register_button = wait.until(EC.element_to_be_clickable(registration_locators.register_button))
        register_button.click()

        wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        assert "https://stellarburgers.nomoreparties.site/login" in driver.current_url

    def test_register_new_user_wrong_password(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        driver.get("https://stellarburgers.nomoreparties.site/")

        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_button))
        login_account_button.click()

        registration_link = wait.until(EC.element_to_be_clickable(login_locators.registration_link))
        registration_link.click()

        name_data = DataHelper.generate_name()
        email_data = DataHelper.generate_login()
        password_data = "123"

        register_name_input = wait.until(EC.visibility_of_element_located(registration_locators.name_input))
        register_email_input = wait.until(EC.visibility_of_element_located(registration_locators.email_input))
        register_password_input = wait.until(EC.visibility_of_element_located(registration_locators.password_input))

        register_name_input.send_keys(name_data)
        register_email_input.send_keys(email_data)
        register_password_input.send_keys(password_data)

        register_button = wait.until(EC.element_to_be_clickable(registration_locators.register_button))
        register_button.click()

        error_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "input__error"))).text
        assert "Некорректный пароль" in error_message