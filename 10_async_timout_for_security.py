import aiohttp
import async_timeout
import asyncio
import time


TARGET_URL = 'https://google.com/'


async def fetch_page(session, url):
    page_start = time.time()
    async with async_timeout.timeout(15):
        async with session.get(url) as response:
            print(f'[{response.status}] Page took {time.time() - page_start}')
            return await response.text()


async def get_multiple_pages(*urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_page(session, url) for url in urls]
        grouped_tasks = await asyncio.gather(*tasks)
        return grouped_tasks


loop = asyncio.get_event_loop()
urls = [TARGET_URL for i in range(1)]

start = time.time()
res = loop.run_until_complete(get_multiple_pages(*urls))
print(f'All took: {time.time() - start}')

print(res)
