# Розробіть сокет-сервер на основі бібліотеки asyncio.
import asyncio

local_host = "127.0.0.1"
local_port = 8888

async def handle_client(reader, writer):
    #Обробляє одного підключеного клієнта.
    address = writer.get_extra_info("peername")

    print(f"Клієнт підключився: {address}")

    welcome_message = (
        "Вітаю! Ви підключилися до сервера.\n"
        "Введіть повідомлення або exit для завершення.\n"
    )

    writer.write(welcome_message.encode("utf-8"))

    await writer.drain()

    try:
        while True:
            # Очікуємо повідомлення від клієнта.
            # readline() читає дані до символу нового рядка.
            data = await reader.readline()

            if not data:
                print(f"Клієнт {address} закрив з'єднання")
                break

            message = data.decode("utf-8", errors="replace").strip()

            print(f"Від {address} отримано: {message}")

            if message.lower() == "exit":
                response = ("З'єднання буде закрито. До побачення!\n")

                writer.write(response.encode("utf-8"))

                await writer.drain()

                break

            response = (f"Сервер отримав повідомлення: {message}\n")

            writer.write(response.encode("utf-8"))

            await writer.drain()
    except ConnectionResetError:
        print(f"Клієнт {address} примусово закрив з'єднання"
        )
    finally:
        writer.close()
        await writer.wait_closed()

        print(f"З'єднання з клієнтом {address} закрито")

async def main():
    server = await asyncio.start_server(handle_client, local_host, local_port)

    addresses = server.sockets

    print(f"Сервер запущено на {local_host}:{local_port}")

    if addresses:
        for socket in addresses:
            print(f"Слухає адресу: {socket.getsockname()}")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nСервер зупинено")