import allure
from locators.feed_locators import FeedPageLocators

from pages.base_page import BasePage
from urls import Urls


class FeedPage(BasePage):

    def open(self):
        self.open_page(Urls.FEED_URL)
        self.wait_for_visibility(FeedPageLocators.TITLE)

    def get_title(self):
        return self.wait_for_visibility(FeedPageLocators.TITLE).text

    @allure.step("Получить счетчик {period}")
    def get_count(self, period):
        locator = FeedPageLocators.TOTAL if period == "total" else FeedPageLocators.TODAY
        return int(self.wait_for_visibility(locator).text)

    @allure.step("Дождаться увеличения счетчика {period}")
    def wait_for_count_increase(self, period, previous):
        def count_increased(driver):
            return self.get_count(period) > previous

        self.wait_for_condition(count_increased, timeout=30)
        return self.get_count(period)

    @allure.step("Дождаться заказа {number} в разделе В работе")
    def wait_for_order_in_progress(self, number):
        def contains_order(driver):
            for item in self.find_elements(FeedPageLocators.IN_PROGRESS):
                if item.text.isdigit() and int(item.text) == number:
                    return True
            return False
        return self.wait_for_condition(contains_order, timeout=30)
