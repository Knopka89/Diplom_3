from selenium.webdriver.common.by import By


class MainPageLocators:
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
