import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from urls import Urls


class LoginPage(BasePage):
    EMAIL = (By.CSS_SELECTOR, "input[type='text']")
    PASSWORD = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    def open(self):
        self.open_page(Urls.LOGIN_URL)

    @allure.step("Войти в аккаунт тестового пользователя")
    def login(self, email, password):
        self.wait_for_visibility(self.EMAIL).send_keys(email)
        self.wait_for_visibility(self.PASSWORD).send_keys(password)
        self.click(self.LOGIN_BUTTON)
        self.wait_for_url(Urls.BASE_URL)
