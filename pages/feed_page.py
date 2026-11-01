import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from urls import Urls


class FeedPage(BasePage):
    TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    TOTAL = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    IN_PROGRESS = (By.CSS_SELECTOR, "ul[class*='OrderFeed_orderListReady'] li")

    def open(self):
        self.open_page(Urls.FEED_URL)
        self.wait_for_visibility(self.TITLE)

    def get_title(self):
        return self.wait_for_visibility(self.TITLE).text

    @allure.step("Получить счетчик {period}")
    def get_count(self, period):
        locator = self.TOTAL if period == "total" else self.TODAY
        return int(self.wait_for_visibility(locator).text)

    @allure.step("Дождаться увеличения счетчика {period}")
    def wait_for_count_increase(self, period, previous):
        def count_increased(driver):
            return self.get_count(period) > previous

        WebDriverWait(self.driver, 30).until(count_increased)
        return self.get_count(period)

    @allure.step("Дождаться заказа {number} в разделе В работе")
    def wait_for_order_in_progress(self, number):
        def contains_order(driver):
            for item in driver.find_elements(*self.IN_PROGRESS):
                if item.text.isdigit() and int(item.text) == number:
                    return True
            return False
        return WebDriverWait(self.driver, 30).until(contains_order)
