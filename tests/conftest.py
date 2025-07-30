import pytest

import data
from methods import PostMethods


@pytest.fixture
def auth_user():
    response = PostMethods.login(data.REGISTERED_USER)
    return response

@pytest.fixture
def get_token():
    response = PostMethods.login(data.REGISTERED_USER)
    assert response.status_code == 200, f"Ошибка авторизации: {response.text}"
    return response.json()["accessToken"]
