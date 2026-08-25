# Створіть UDP-сервер, який очікує на повідомлення про нові пристрої в мережі. Він приймає повідомлення певного
# формату, де буде ідентифікатор пристрою, і друкує нові під'єднання в консоль. Створіть UDP-клієнта, який надсилатиме
# унікальний ідентифікатор пристрою на сервер, повідомляючи про свою присутність.
import socket
import uuid

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5006

device_id = str(uuid.uuid4())
message = f"DEVICE_ID:{device_id}"

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    client.sendto(message.encode("utf-8"), (SERVER_IP, SERVER_PORT))
    print(f"Sent: {message}")