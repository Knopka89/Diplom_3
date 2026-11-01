import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from data import TestData
from pages.base_page import BasePage
from urls import Urls


class MainPage(BasePage):
    INGREDIENT = (By.XPATH, "//a[@draggable='true'][p[text()='{}']]")
    INGREDIENT_COUNTER = (
        By.XPATH,
        "//a[@draggable='true'][p[text()='{}']]//p[contains(@class,'counter_counter__num')]",
    )
    TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    DROP_AREA = (By.CSS_SELECTOR, ".constructor-element_pos_top")
    DETAILS_TITLE = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]//h2")
    DETAILS_NAME = (By.CSS_SELECTOR, "section[class*='Modal_modal_opened'] div[class*='Modal_modal__contentBox'] > p")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER = (By.CSS_SELECTOR, "section[class*='Modal_modal_opened'] h2")

    def open(self):
        self.open_page(Urls.BASE_URL)
        self.wait_for_visibility(self.TITLE)

    def ingredient_locator(self, name):
        return self.format_locator(self.INGREDIENT, name)

    def counter_locator(self, name):
        return self.format_locator(self.INGREDIENT_COUNTER, name)

    def get_title(self):
        return self.wait_for_visibility(self.TITLE).text

    @allure.step("Открыть детали ингредиента {name}")
    def open_ingredient(self, name):
        self.click(self.ingredient_locator(name))
        return self.wait_for_visibility(self.DETAILS_TITLE).text

    def get_ingredient_name(self):
        return self.wait_for_visibility(self.DETAILS_NAME).text

    def get_counter(self, name):
        return int(self.wait_for_visibility(self.counter_locator(name)).text)

    @allure.step("Добавить ингредиент {name} в заказ")
    def add_ingredient(self, name):
        ingredient = self.wait_for_visibility(self.ingredient_locator(name))
        target = self.wait_for_visibility(self.DROP_AREA)

        if self.driver.capabilities["browserName"] == "firefox":
            self.driver.execute_script("""
                const source = arguments[0];
                const target = arguments[1];
                const dataTransfer = new DataTransfer();

                function send(element, type) {
                    const rect = element.getBoundingClientRect();
                    element.dispatchEvent(new DragEvent(type, {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer,
                        clientX: rect.left + rect.width / 2,
                        clientY: rect.top + rect.height / 2
                    }));
                }

                send(source, "dragstart");
                send(target, "dragenter");
                send(target, "dragover");
                send(target, "drop");
                send(source, "dragend");
            """, ingredient, target)
        else:
            ActionChains(self.driver).drag_and_drop(
                ingredient, target
            ).perform()

    def wait_for_counter(self, name, expected):
        def counter_matches(driver):
            return self.get_counter(name) == expected

        return WebDriverWait(self.driver, 15).until(counter_matches)

    @allure.step("Собрать бургер и оформить заказ")
    def create_order(self):
        self.add_ingredient(TestData.BUN)
        self.wait_for_counter(TestData.BUN, 2)
        self.add_ingredient(TestData.FILLING)
        self.wait_for_counter(TestData.FILLING, 1)
        self.click(self.ORDER_BUTTON)
        return WebDriverWait(self.driver, 45).until(self.read_order_number)

    def read_order_number(self, driver):
        elements = driver.find_elements(*self.ORDER_NUMBER)
        if elements and elements[0].is_displayed():
            text = elements[0].text
            if text.isdigit() and int(text) > 0 and text != "9999":
                return int(text)
        return False
