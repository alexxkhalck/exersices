# Створіть сокет, який приймає повідомлення з двома числами, що розділені комою. Сервер має конвертувати рядкове повідомлення у два
# числа й обчислювати його суму. Після успішного обчислення повертати відповідь клієнту.
import socket

HOST = "127.0.0.1"
PORT = 5006

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(1)

    print(f"Сервер очікує підключення на {HOST}:{PORT}")

    connection, address = server.accept()

    with connection:
        print(f"Підключився клієнт: {address}")

        data = connection.recv(1024)
        message = data.decode("utf-8").strip()

        try:
            numbers = list(map(float, message.split(",")))

            if len(numbers) != 2:
                raise ValueError

            result = numbers[0] + numbers[1]
            response = f"Сума: {result}"

        except ValueError:
            response = "Помилка: потрібно надіслати два числа через кому"

        connection.sendall(response.encode("utf-8"))

# import socket

# HOST = "127.0.0.1"
# PORT = 5006

message = input("Введіть два числа через кому: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(message.encode("utf-8"))

    data = client.recv(1024)

print(data.decode("utf-8"))