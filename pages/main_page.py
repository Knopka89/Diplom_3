import allure
from locators.main_locators import MainPageLocators

from data import TestData
from pages.base_page import BasePage
from urls import Urls


class MainPage(BasePage):

    def open(self):
        self.open_page(Urls.BASE_URL)
        self.wait_for_visibility(MainPageLocators.TITLE)

    def ingredient_locator(self, name):
        return self.format_locator(MainPageLocators.INGREDIENT, name)

    def counter_locator(self, name):
        return self.format_locator(MainPageLocators.INGREDIENT_COUNTER, name)

    def get_title(self):
        return self.wait_for_visibility(MainPageLocators.TITLE).text

    @allure.step("Открыть детали ингредиента {name}")
    def open_ingredient(self, name):
        self.click(self.ingredient_locator(name))
        return self.wait_for_visibility(MainPageLocators.DETAILS_TITLE).text

    def get_ingredient_name(self):
        return self.wait_for_visibility(MainPageLocators.DETAILS_NAME).text

    def get_counter(self, name):
        return int(self.wait_for_visibility(self.counter_locator(name)).text)

    @allure.step("Добавить ингредиент {name} в заказ")
    def add_ingredient(self, name):
        ingredient = self.wait_for_visibility(self.ingredient_locator(name))
        target = self.wait_for_visibility(MainPageLocators.DROP_AREA)

        self.drag_ingredient(ingredient, target)

    def wait_for_counter(self, name, expected):
        def counter_matches(driver):
            return self.get_counter(name) == expected

        return self.wait_for_condition(counter_matches)

    @allure.step("Собрать бургер и оформить заказ")
    def create_order(self):
        self.add_ingredient(TestData.BUN)
        self.wait_for_counter(TestData.BUN, 2)
        self.add_ingredient(TestData.FILLING)
        self.wait_for_counter(TestData.FILLING, 1)
        self.click(MainPageLocators.ORDER_BUTTON)
        return self.wait_for_condition(self.read_order_number, timeout=45)

    def read_order_number(self, driver):
        elements = self.find_elements(MainPageLocators.ORDER_NUMBER)
        if elements and elements[0].is_displayed():
            text = elements[0].text
            if text.isdigit() and int(text) > 0 and text != "9999":
                return int(text)
        return False
