import helper

NEW_USER = {
    "email": helper.mail_generator(),
    "password": helper.fake_password(),
    "name": helper.fake_firstname()
}

OLD_USER = {
    "email": "testdataggg@yandex.ru",
    "password": "123123",
    "name": "Username"
}

NON_FIELD_USER = {
    "email": helper.mail_generator(),
    "password": "",
    "name": helper.fake_firstname()
}

REGISTERED_USER = {
    "email": "testdataggg@yandex.ru",
    "password": "123123"
}

ERROR_USER = {
    "email": "dataggg@yandex.ru",
    "password": "321321"
}

INGREDIENTS = [
    "61c0c5a71d1f82001bdaaa6d", #"Флюоресцентная булка R2-D3"
    "61c0c5a71d1f82001bdaaa70", # "Говяжий метеорит (отбивная)"
    "61c0c5a71d1f82001bdaaa72" # "Соус Spicy-X"
]

INGREDIENTS_NON = []

INGREDIENTS_INVALID = ["123"]