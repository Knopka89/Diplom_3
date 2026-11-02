import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from helpers import generate_user_data, register_user, delete_user


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        browser = webdriver.Chrome(options=options)
    else:
        options = webdriver.FirefoxOptions()
        browser = webdriver.Firefox(options=options)
    browser.set_window_size(1440, 1000)
    yield browser
    browser.quit()


@pytest.fixture
def registered_user():
    data = generate_user_data()
    token = register_user(data)
    yield data
    delete_user(token)


@pytest.fixture
def authorized_driver(driver, registered_user):
    page = LoginPage(driver)
    page.open()
    page.login(registered_user["email"], registered_user["password"])
    return driver
