# Створіть HTTP-клієнта, який прийматиме URL ресурсу, тип методу та словник як передавальні дані (опціональний).
# Виконувати запит з отриманим методом на отриманий ресурс, передаючи дані відповідним методом, та друкувати на
# консоль статус-код, заголовки та тіло відповіді.
import requests


def http_client(url, method, data=None):
    method = method.upper()

    if data is None:
        data = {}

    try:
        if method in ("GET", "HEAD"):
            response = requests.request(
                method=method,
                url=url,
                params=data,
                timeout=10
            )
        else:
            response = requests.request(
                method=method,
                url=url,
                json=data,
                timeout=10
            )

        print("Статус-код:")
        print(response.status_code)

        print("\nЗаголовки:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")

        print("\nТіло відповіді:")
        print(response.text)

    except requests.exceptions.RequestException as error:
        print(f"Помилка під час виконання запиту: {error}")