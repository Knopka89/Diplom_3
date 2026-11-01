import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    CONSTRUCTOR_LINK = (By.XPATH, "//a[p[text()='Конструктор']]")
    FEED_LINK = (By.CSS_SELECTOR, "a[href='/feed']")
    MODAL = (By.CSS_SELECTOR, "section[class*='Modal_modal_opened']")
    CLOSE_MODAL = (By.CSS_SELECTOR, "section[class*='Modal_modal_opened'] button")
    MODAL_OVERLAY = (By.CSS_SELECTOR, "div[class*='Modal_modal_overlay']")

    def __init__(self, driver):
        self.driver = driver

    def format_locator(self, locator, value):
        return (locator[0], locator[1].format(value))

    def is_modal_closed(self):
        return not self.driver.find_elements(*self.MODAL)

    @allure.step("Открыть страницу {url}")
    def open_page(self, url):
        self.driver.get(url)

    def wait_for_visibility(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Нажать на элемент {locator}")
    def click(self, locator):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Закрыть всплывающее окно")
    def close_modal(self):
        self.click(self.CLOSE_MODAL)
        WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(self.MODAL))
        WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(self.MODAL_OVERLAY))

    def wait_for_url(self, url):
        WebDriverWait(self.driver, 15).until(EC.url_to_be(url))
        return self.driver.current_url

    @allure.step("Перейти в конструктор")
    def click_constructor(self):
        self.click(self.CONSTRUCTOR_LINK)

    @allure.step("Перейти в ленту заказов")
    def click_feed(self):
        self.click(self.FEED_LINK)
