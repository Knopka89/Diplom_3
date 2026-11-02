import allure
from locators.login_locators import LoginPageLocators

from pages.base_page import BasePage
from urls import Urls


class LoginPage(BasePage):

    def open(self):
        self.open_page(Urls.LOGIN_URL)

    @allure.step("Войти в аккаунт тестового пользователя")
    def login(self, email, password):
        self.wait_for_visibility(LoginPageLocators.EMAIL).send_keys(email)
        self.wait_for_visibility(LoginPageLocators.PASSWORD).send_keys(password)
        self.click(LoginPageLocators.LOGIN_BUTTON)
        self.wait_for_url(Urls.BASE_URL)
