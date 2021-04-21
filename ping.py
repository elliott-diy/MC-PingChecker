import asyncio
import urllib.parse
from colorama import init, Fore
from time import perf_counter

init(autoreset=True)


async def check(url: str):
    async def x():
        uri = urllib.parse.urlparse(url)
        reader, writer = await asyncio.open_connection(uri.hostname, 443, ssl=True)
        writer.write(f"GET {uri.path or '/'} HTTP/1.1\r\nHost:{uri.hostname}\r\n\r\n".encode())

        start = perf_counter()
        await writer.drain()

        await reader.read(1)
        end = perf_counter()
        return round((end - start) * 1000)

    pings = []

    for _ in range(5):
        pings.append(await x())
        await asyncio.sleep(0.01)

    print(f"{Fore.GREEN}Minecraft API {Fore.LIGHTBLACK_EX}- {Fore.RED}{urllib.parse.urlparse(url).hostname}")
    print(f"{Fore.CYAN}Your Ping {Fore.LIGHTBLACK_EX}- {Fore.RED}{sum(pings)/5}ms")
    print()


async def main():
    await check("https://api.minecraftservices.com/minecraft")
    await check("https://api.mojang.com")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())