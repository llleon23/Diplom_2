import allure
import data
from methods import PostMethods


@allure.title("Создание заказа")
class TestAuthLogin:
    @allure.step("Создание заказа с авторизацией")
    def test_order_create_with_auth(self, get_token):
        order_data = {"ingredients": data.INGREDIENTS}
        response = PostMethods.create_order(order_data, get_token)
        assert response.status_code == 200, \
            f"Ожидаем код 200, получен {response.status_code}"
        assert response.json().get("success") == True
        assert "order" in response.json(), "В ответе отсутствует номер заказа"

    @allure.step("Создание заказа без авторизации")
    def test_order_create_non_auth(self):
        order_data = {"ingredients": data.INGREDIENTS}
        response = PostMethods.create_order(order_data)
        assert response.status_code == 200, \
            f"Ожидался код 200, получен {response.status_code}. "
        assert response.json().get("success") == True

    @allure.step("Создание заказа с ингредиентами")
    def test_order_create_with_ingr(self):
        order_data = {"ingredients": data.INGREDIENTS}
        response = PostMethods.create_order(order_data)
        assert response.status_code == 200, \
            f"Ожидался код 200, получен {response.status_code}. "
        assert response.json().get("success") == True

    @allure.step("Создание заказа без ингредиентов")
    def test_order_create_with_ingr_non(self):
        order_data = {"ingredients": data.INGREDIENTS_NON}
        response = PostMethods.create_order(order_data)
        assert response.status_code == 400, \
            f"Ожидался код 400, получен {response.status_code}. "
        assert response.json().get("success") == False

    @allure.step("Создание заказа с неверным хешем ингредиентов")
    def test_order_create_with_ingr_invalid(self):
        order_data = {"ingredients": data.INGREDIENTS_INVALID}
        response = PostMethods.create_order(order_data)
        assert response.status_code == 500, \
            f"Ожидался код 500, получен {response.status_code}. "
