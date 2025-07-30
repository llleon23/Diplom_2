import allure
import data
from methods import PostMethods


@allure.story("Авторизация пользователя")
class TestAuthLogin:
    @allure.title("Вход под существующим пользователем")
    def test_auth_login_old_user(self):
        with allure.step("Отправка запроса на авторизацию существующего пользователя"):
            response = PostMethods.login(data.REGISTERED_USER)

        with allure.step("Проверка кода ответа"):
            assert response.status_code == 200, \
                f"Ожидаем код 200, получен {response.status_code}"

        with allure.step("Проверка флага success в ответе"):
            assert response.json().get("success") == True, \
                f"Ожидаем сообщение: 'True', получаем: {response.json().get('success')}"

        with allure.step("Проверка данных ответа"):
            response_data = response.json()
            user_data = response_data.get("user", {})
            assert "refreshToken" in response_data
            assert response_data["accessToken"].startswith("Bearer "), \
                f"accessToken должен начинаться с 'Bearer ', получен: '{response_data['accessToken']}'"
            assert user_data["email"] == data.OLD_USER["email"], \
                f"Ожидаем email: {user_data['email']}, получен: {response.json().get('user', {}).get('email')}"
            assert user_data["name"] == data.OLD_USER["name"], \
                f"Ожидаем name: {user_data['name']}, получен: {response.json().get('user', {}).get('name')}"

    @allure.title("Вход с неверным логином и паролем")
    def test_auth_login_error_user_data(self):
        with allure.step("Отправка запроса на авторизацию с неверными данными"):
            response = PostMethods.login(data.ERROR_USER)

        with allure.step("Проверка кода ответа"):
            assert response.status_code == 401, \
                f"Ожидаем код 401, получен {response.status_code}"

        with allure.step("Проверка флага success в ответе"):
            assert response.json().get("success") == False, \
                f"Ожидаем сообщение: 'False', получаем: {response.json().get('success')}"

        with allure.step("Проверка сообщения об ошибке"):
            assert response.json().get("message") == "email or password are incorrect", \
                f"Ожидаем сообщение: 'email or password are incorrect', получаем: {response.json().get('message')}"


    @allure.title("Вход с неверным паролем")
    def test_auth_login_error_password(self):
        with allure.step("Отправка запроса на авторизацию с неверным паролем"):
            response = PostMethods.login(data.ERROR_USER_PASSWORD)

        with allure.step("Проверка кода ответа"):
            assert response.status_code == 401, \
                f"Ожидаем код 401, получен {response.status_code}"

        with allure.step("Проверка флага success в ответе"):
            assert response.json().get("success") == False, \
                f"Ожидаем сообщение: 'False', получаем: {response.json().get('success')}"

        with allure.step("Проверка сообщения об ошибке"):
            assert response.json().get("message") == "email or password are incorrect", \
                f"Ожидаем сообщение: 'email or password are incorrect', получаем: {response.json().get('message')}"
