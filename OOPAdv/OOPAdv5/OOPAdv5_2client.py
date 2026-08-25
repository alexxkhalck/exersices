# Розробіть сокет-сервер на основі бібліотеки asyncio.
import asyncio

local_host = "127.0.0.1"
local_port = 8888

async def main():
    reader, writer = await asyncio.open_connection(local_host, local_port)

    try:
        welcome_message = await reader.readline()

        print(welcome_message.decode("utf-8", errors="replace").strip())

        while True:
            message = input("Введіть повідомлення: ")

            writer.write(f"{message}\n".encode("utf-8"))

            await writer.drain()

            response = await reader.readline()

            if not response:
                break

            print("Відповідь сервера:", response.decode("utf-8", errors="replace").strip())

            if message.lower() == "exit":
                break

    finally:
        writer.close()
        await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())