from selenium.webdriver.common.by import By


class HomePageLocators: # Главная страница сайта
    login_account_button = (By.XPATH, "//button[text() = 'Войти в аккаунт']") # Кнопка "Войти в аккаунт"
    account_link = (By.XPATH, "//a[@href = '/account']") # Ссылка на личный кабинет
    constructor_link = (By.XPATH, "//a[@href = '/']") # Ссылка на конструктор
    stellar_burgers_logo = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']") # Ссылка на логотип
    buns_button = (By.XPATH, "//span[text() = 'Булки']") # Кнопка "Булки"
    sauces_button = (By.XPATH, "//span[text() = 'Соусы']") # Кнопка "Соусы"
    fillings_button = (By.XPATH, "//span[text() = 'Начинки']") # Кнопка "Начинки"
    buns_title = (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10' and text() = 'Булки']") # Заголовок "Булки"
    sauces_title = (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10' and text() = 'Соусы']")  # Заголовок "Соусы"
    fillings_title = (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10' and text() = 'Начинки']")  # Заголовок "Начинки"

class LoginPageLocators: # Страница входа на сайт
    login_label = (By.XPATH, "//h2[text() = 'Вход']") # Заголовок "Вход"
    login_input = (By.XPATH, "//label[text() = 'Email']/following-sibling::input") # Поле ввода почты
    password_input = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input") # Поле ввода пароля
    login_button = (By.XPATH, "//button[text() = 'Войти']") # Кнопка "Войти"
    registration_link = (By.XPATH, "//a[@href = '/register']") # Ссылка "Зарегистрироваться"
    restore_password_link = (By.XPATH, "//a[@href = '/forgot-password']") # Ссылка "Восстановить пароль"

class RegistrationPageLocators: # Страница регистрации
    name_input = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input") # Поле ввода имени
    email_input = (By.XPATH, "//label[text() = 'Email']/following-sibling::input") # Поле ввода почты
    password_input = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input") # Поле ввода пароля
    register_button = (By.XPATH, "//button[text() = 'Зарегистрироваться']") # Кнопка "Зарегистрироваться"
    login_link = (By.XPATH, "//a[@href = '/login']") # Ссылка "Войти"

class AccountPageLocators: # Личный кабинет
    name_input = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input") # Поле ввода имени
    login_input = (By.XPATH, "//label[text() = 'Логин']/following-sibling::input") # Поле ввода почты
    password_input = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input") # Поле ввода пароля
    logout_button = (By.XPATH, "//button[text() = 'Выход']") # Кнопка "Выйти"

class ForgotPasswordLocators: # Страница восстановления пароля
    login_link = (By.XPATH, "//a[@href = '/login']") # Ссылка "Войти"





