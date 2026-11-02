from selenium.webdriver.common.by import By


class FeedPageLocators:
    TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    TOTAL = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    IN_PROGRESS = (By.CSS_SELECTOR, "ul[class*='OrderFeed_orderListReady'] li")
