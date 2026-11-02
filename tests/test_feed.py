import allure
import pytest

from pages.feed_page import FeedPage
from pages.main_page import MainPage


class TestFeed:
    @allure.title("Новый заказ увеличивает счетчик выполненных заказов")
    @pytest.mark.parametrize("period", ["total", "today"])
    def test_order_counter_increases(self, authorized_driver, period):
        feed = FeedPage(authorized_driver)
        feed.open()
        before = feed.get_count(period)
        feed.click_constructor()
        main = MainPage(authorized_driver)

        main.create_order()
        main.close_modal()
        main.click_feed()

        after = feed.wait_for_count_increase(period, before)
        assert after > before

    @allure.title("Номер оформленного заказа появляется в разделе В работе")
    def test_order_number_in_progress(self, authorized_driver):
        main = MainPage(authorized_driver)

        number = main.create_order()
        main.close_modal()
        main.click_feed()

        assert FeedPage(authorized_driver).wait_for_order_in_progress(number)
