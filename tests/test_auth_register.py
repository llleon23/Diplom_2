import allure
import data
from methods import PostMethods


@allure.story("Тесты на создание пользователя")
class TestAuthRegister:
    @allure.title("Создание нового пользователя")
    def test_auth_register_create_new_user(self):
        with allure.step("POST /api/auth/register → 200 (успешная регистрация)"):
            response = PostMethods.register(data.NEW_USER)

        with allure.step("Проверка ответа"):
            assert response.status_code == 200, f"Фактический код: {response.status_code}"
            assert response.json()["success"] is True
            assert "refreshToken" in response.json()
            assert response.json()["accessToken"].startswith("Bearer ")
            assert response.json()["user"]["email"] == data.NEW_USER["email"]
            assert response.json()["user"]["name"] == data.NEW_USER["name"]

    @allure.title("Регистрация уже существующего пользователя")
    def test_auth_register_create_old_user(self):
        with allure.step("POST /api/auth/register → 403 (пользователь уже существует)"):
            response = PostMethods.register(data.OLD_USER)

        with allure.step("Проверка ошибки"):
            assert response.status_code == 403
            assert response.json()["success"] is False
            assert response.json()["message"] == "User already exists"

    @allure.title("Создание пользователя без обязательного поля 'Пароль'")
    def test_auth_register_create_new_user_non_password(self):
        with allure.step("POST /api/auth/register → 403 (не заполнено поле)"):
            response = PostMethods.register(data.NON_FIELD_PASS_USER)

        with allure.step("Проверка ошибки"):
            assert response.status_code == 403
            assert response.json()["success"] is False
            assert response.json()["message"] == "Email, password and name are required fields"

    @allure.title("Создание пользователя без обязательного поля 'EMAIL'")
    def test_auth_register_create_new_user_non_field_email(self):
        with allure.step("POST /api/auth/register → 403 (не заполнено поле)"):
            response = PostMethods.register(data.NON_FIELD_EMAIL_USER)

        with allure.step("Проверка ошибки"):
            assert response.status_code == 403
            assert response.json()["success"] is False
            assert response.json()["message"] == "Email, password and name are required fields"

    @allure.title("Создание пользователя без обязательного поля 'NAME'")
    def test_auth_register_create_new_user_non_field_name(self):
        with allure.step("POST /api/auth/register → 403 (не заполнено поле)"):
            response = PostMethods.register(data.NON_FIELD_NAME)

        with allure.step("Проверка ошибки"):
            assert response.status_code == 403
            assert response.json()["success"] is False
            assert response.json()["message"] == "Email, password and name are required fields"
