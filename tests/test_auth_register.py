import allure

import data
from methods import PostMethods

@allure.title("Тесты на создание пользователя")
class TestAuthRegister:
    @allure.step("Тест на создание нового пользователя")
    def test_auth_register_create_new_user(self):
        response = PostMethods.register(data.NEW_USER)
        assert response.status_code == 200, \
            f"Ожидаем код 200, получен {response.status_code}"

        assert response.json().get("success") == True, \
            f"Ожидаем сообщение: 'True', получаем: {response.json().get("success")}"

        response_data = response.json()
        user_data = response_data.get("user", {})

        assert "refreshToken" in response_data
        assert response_data["accessToken"].startswith("Bearer "), \
    f"accessToken должен начинаться с 'Bearer ', получен: '{response_data['accessToken']}'"

        assert user_data["email"] == data.NEW_USER["email"], \
            f"Ожидаем email: {user_data["email"]}, получен: {response.json().get('user', {}).get('email')}"

        assert user_data["name"] == data.NEW_USER["name"], \
            f"Ожидаем name: {user_data["name"]}, получен: {response.json().get('user', {}).get("name")}"

    @allure.step("Тест на создание пользователя, который уже зарегистрирован")
    def test_auth_register_create_old_user(self):
        response = PostMethods.register(data.OLD_USER)
        assert response.status_code == 403, \
            f"Ожидаем код 403, получен {response.status_code}"
        assert response.json().get("success") == False, \
            f"Ожидаем сообщение: 'False', получаем: {response.json().get("success")}"
        assert response.json().get("message") == "User already exists", \
            f"Ожидаем сообщение: 'User already exists', получаем: {response.json().get("message")}"

    @allure.step("Тест на создание пользователя и не заполнение одно из обязательных полей.")
    def test_auth_register_create_new_user_non_field(self):
        response = PostMethods.register(data.NON_FIELD_USER)
        assert response.status_code == 403, \
            f"Ожидаем код 403, получен {response.status_code}"
        assert response.json().get("success") == False, \
            f"Ожидаем сообщение: 'False', получаем: {response.json().get("success")}"
        assert response.json().get("message") == "Email, password and name are required fields", \
            f"Ожидаем сообщение: 'Email, password and name are required fields', получаем: {response.json().get("message")}"
