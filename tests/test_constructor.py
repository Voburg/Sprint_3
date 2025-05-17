from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.all_locators import (
    HomePageLocators,
)

home_locators = HomePageLocators()

class TestConstructor:
    def test_transition_to_ingredient_buns(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        driver.get("https://stellarburgers.nomoreparties.site/")

        fillings_button = wait.until(EC.element_to_be_clickable(home_locators.fillings_button))
        fillings_button.click()

        buns_button = wait.until(EC.element_to_be_clickable(home_locators.buns_button))
        buns_button.click()

        buns = wait.until(EC.visibility_of_element_located(home_locators.buns_title))
        assert buns.text == "Булки"

    def test_transition_to_ingredient_fillings(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        driver.get("https://stellarburgers.nomoreparties.site/")

        fillings_button = wait.until(EC.element_to_be_clickable(home_locators.fillings_button))
        fillings_button.click()

        fillings = wait.until(EC.visibility_of_element_located(home_locators.fillings_title))
        assert fillings.text == "Начинки"

    def test_transition_to_ingredient_souses(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        driver.get("https://stellarburgers.nomoreparties.site/")

        fillings = wait.until(EC.element_to_be_clickable(home_locators.fillings_button))
        fillings.click()

        souses_button = wait.until(EC.element_to_be_clickable(home_locators.sauces_button))
        souses_button.click()

        souses = wait.until(EC.visibility_of_element_located(home_locators.sauces_title))
        assert souses.text == "Соусы"