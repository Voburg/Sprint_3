from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


class TestIngredients:
    def test_go_to_ingredient_souses(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        driver.get("https://stellarburgers.nomoreparties.site/")
        sleep(3)

        fillings = wait.until(EC.element_to_be_clickable(home_locators.fillings))
        fillings.click()
        sleep(3)

        souses = wait.until(EC.element_to_be_clickable(home_locators.sauces))
        souses.click()
        sleep(3)

        souses = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10' and text() = 'Соусы']")))
        assert souses.text == "Соусы"

        driver.quit()