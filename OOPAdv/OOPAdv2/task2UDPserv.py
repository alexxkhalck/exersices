# Створіть UDP-сервер, який очікує на повідомлення про нові пристрої в мережі. Він приймає повідомлення певного формату, де буде
# ідентифікатор пристрою, і друкує нові під'єднання в консоль. Створіть UDP-клієнта, який надсилатиме унікальний
# ідентифікатор пристрою на сервер, повідомляючи про свою присутність.
import socket

HOST = "127.0.0.1"
PORT = 5006
SERVER_IP = "127.0.0.1"
SERVER_PORT = 5006

seen_devices = set()

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.bind((HOST, PORT))
    print(f"UDP server listening on {HOST}:{PORT}")

    while True:
        data, addr = server.recvfrom(1024)
        message = data.decode("utf-8").strip()

        if message.startswith("DEVICE_ID:"):
            device_id = message.split(":", 1)[1]

            if device_id not in seen_devices:
                seen_devices.add(device_id)
                print(f"New device connected: {device_id} from {addr[0]}:{addr[1]}")
            else:
                print(f"Known device: {device_id} from {addr[0]}:{addr[1]}")
        else:
            print(f"Invalid message from {addr}: {message}")