import requests

import curl


class PostMethods:
    @staticmethod
    def register(user_data):
        return requests.post(curl.REGISTER, json= user_data)

    @staticmethod
    def login(user_data):
        headers = {"Content-Type": "application/json"}
        return requests.post(
            curl.LOGIN,
            json=user_data,
            headers=headers
        )

    @staticmethod
    def create_order(order_data, token=None):
        headers = {"Content-Type": "application/json"}
        if token:
            headers["Authorization"] = token

        response = requests.post(
            curl.CREATE_ORDER,
            json=order_data,
            headers=headers
        )
        return response

