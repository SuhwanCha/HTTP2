import aiohttp
import asyncio
import timeit

async def fetch(url):
    print('Start', url)
    req = await aiohttp.request('GET', url)
    print('Done', url)

async def fetch_all(urls):
    fetches = [asyncio.Task(fetch(url)) for url in urls]
    await asyncio.gather(*fetches)

urls = ['http://b.ssut.me', 'https://google.com', 'https://apple.com', 'https://ubit.info', 'https://github.com/ssut']

start = timeit.default_timer()
loop = asyncio.get_event_loop()
loop.run_until_complete(fetch_all(urls))
duration = timeit.default_timer() - start
