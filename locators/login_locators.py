from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL = (By.CSS_SELECTOR, "input[type='text']")
    PASSWORD = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
