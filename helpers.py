import random
import string

import allure
import requests

from urls import Urls


def generate_random_string(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def generate_user_data():
    return {
        "email": "qa_ui_" + generate_random_string(15) + "@example.com",
        "password": generate_random_string(15),
        "name": "Test",
    }


@allure.step("Создать тестового пользователя")
def register_user(data):
    response = requests.post(Urls.REGISTER_API, json=data, timeout=30)
    assert response.status_code == 200
    return response.json()["accessToken"]


@allure.step("Удалить тестового пользователя")
def delete_user(token):
    response = requests.delete(
        Urls.USER_API, headers={"Authorization": token}, timeout=30
    )
    assert response.status_code == 202
