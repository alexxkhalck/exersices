# Створити простий чат на основі протоколу TCP, який дасть змогу під'єднуватися кільком клієнтам та
# обмінюватися повідомленнями.
import socket
import threading

HOST = "127.0.0.1"
PORT = 5006

clients = {}
clients_lock = threading.Lock()


def broadcast(message, sender_socket=None):
    data = (message + "\n").encode("utf-8")

    with clients_lock:
        connected_clients = list(clients.keys())

    for client_socket in connected_clients:
        if client_socket != sender_socket:
            try:
                client_socket.sendall(data)
            except OSError:
                remove_client(client_socket)


def remove_client(client_socket):
    with clients_lock:
        username = clients.pop(client_socket, None)

    try:
        client_socket.close()
    except OSError:
        pass

    if username:
        print(f"{username} від'єднався")
        broadcast(f"[Система] {username} залишив чат")


def handle_client(client_socket, address):
    reader = client_socket.makefile(
        "r",
        encoding="utf-8",
        newline="\n"
    )

    try:
        username = reader.readline().strip()

        if not username:
            return

        with clients_lock:
            clients[client_socket] = username

        print(f"{username} під'єднався: {address}")
        broadcast(f"[Система] {username} приєднався до чату")

        for line in reader:
            message = line.strip()

            if not message:
                continue

            if message == "/quit":
                break

            print(f"{username}: {message}")
            broadcast(f"{username}: {message}", client_socket)

    except (ConnectionResetError, OSError):
        pass

    finally:
        remove_client(client_socket)
        reader.close()


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()

        print(f"Сервер запущено на {HOST}:{PORT}")

        while True:
            client_socket, address = server.accept()

            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, address),
                daemon=True
            )
            client_thread.start()


if __name__ == "__main__":
    start_server()

import socket
import threading

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000


def receive_messages(client_socket):
    reader = client_socket.makefile(
        "r",
        encoding="utf-8",
        newline="\n"
    )

    try:
        for line in reader:
            print(line.rstrip())
    except OSError:
        pass
    finally:
        reader.close()


def send_messages(client_socket, username):
    try:
        while True:
            message = input()

            client_socket.sendall(
                (message + "\n").encode("utf-8")
            )

            if message == "/quit":
                break

    except (OSError, EOFError):
        pass


def start_client():
    username = input("Введіть ім'я: ").strip()

    if not username:
        username = "Анонім"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((SERVER_HOST, SERVER_PORT))

        client.sendall(
            (username + "\n").encode("utf-8")
        )

        receive_thread = threading.Thread(
            target=receive_messages,
            args=(client,),
            daemon=True
        )
        receive_thread.start()

        send_messages(client, username)


if __name__ == "__main__":
    start_client()