import allure
import data
from methods import PostMethods


@allure.title("Авторизация пользователя")
class TestAuthLogin:
    @allure.step("Вход под существующим пользователем")
    def test_auth_login_old_user(self):
        response = PostMethods.login(data.REGISTERED_USER)
        assert response.status_code == 200, \
            f"Ожидаем код 200, получен {response.status_code}"
        assert response.json().get("success") == True, \
            f"Ожидаем сообщение: 'True', получаем: {response.json().get("success")}"
        response_data = response.json()
        user_data = response_data.get("user", {})
        assert "refreshToken" in response_data
        assert response_data["accessToken"].startswith("Bearer "), \
    f"accessToken должен начинаться с 'Bearer ', получен: '{response_data['accessToken']}'"
        assert user_data["email"] == data.OLD_USER["email"], \
            f"Ожидаем email: {user_data["email"]}, получен: {response.json().get('user', {}).get('email')}"
        assert user_data["name"] == data.OLD_USER["name"], \
            f"Ожидаем name: {user_data["name"]}, получен: {response.json().get('user', {}).get("name")}"

    @allure.step("Вход с неверным логином и паролем.")
    def test_auth_login_registered_user(self):
        response = PostMethods.login(data.ERROR_USER)
        assert response.status_code == 401, \
            f"Ожидаем код 403, получен {response.status_code}"
        assert response.json().get("success") == False, \
            f"Ожидаем сообщение: 'False', получаем: {response.json().get("success")}"
        assert response.json().get("message") == "email or password are incorrect", \
            f"Ожидаем сообщение: 'Email, password and name are required fields', получаем: {response.json().get("message")}"
