from selenium.webdriver.common.by import By


class BasePageLocators:
    CONSTRUCTOR_LINK = (By.XPATH, "//a[p[text()='Конструктор']]")
    FEED_LINK = (By.CSS_SELECTOR, "a[href='/feed']")
    MODAL = (By.CSS_SELECTOR, "section[class*='Modal_modal_opened']")
    CLOSE_MODAL = (By.CSS_SELECTOR, "section[class*='Modal_modal_opened'] button")
    MODAL_OVERLAY = (By.CSS_SELECTOR, "div[class*='Modal_modal_overlay']")
