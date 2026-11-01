import allure

from data import TestData
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from urls import Urls


class TestConstructor:
    @allure.title("Переход в конструктор из ленты заказов")
    def test_open_constructor(self, driver):
        feed = FeedPage(driver)
        feed.open()
        feed.click_constructor()

        assert feed.wait_for_url(Urls.BASE_URL) == Urls.BASE_URL
        assert MainPage(driver).get_title() == "Соберите бургер"

    @allure.title("Переход из конструктора в ленту заказов")
    def test_open_feed(self, driver):
        page = MainPage(driver)
        page.open()
        page.click_feed()

        assert page.wait_for_url(Urls.FEED_URL) == Urls.FEED_URL
        assert FeedPage(driver).get_title() == "Лента заказов"

    @allure.title("Клик по ингредиенту открывает его детали")
    def test_open_ingredient_details(self, driver):
        page = MainPage(driver)
        page.open()

        assert page.open_ingredient(TestData.BUN) == "Детали ингредиента"
        assert page.get_ingredient_name() == TestData.BUN

    @allure.title("Крестик закрывает окно ингредиента")
    def test_close_ingredient_details(self, driver):
        page = MainPage(driver)
        page.open()
        page.open_ingredient(TestData.BUN)

        page.close_modal()

        assert page.is_modal_closed()

    @allure.title("При добавлении ингредиента его счетчик увеличивается")
    def test_ingredient_counter_increases(self, driver):
        page = MainPage(driver)
        page.open()
        before = page.get_counter(TestData.BUN)

        page.add_ingredient(TestData.BUN)

        assert page.wait_for_counter(TestData.BUN, before + 2)
