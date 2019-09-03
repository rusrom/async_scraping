import aiohttp
import asyncio
import time


TARGET_URL = 'https://google.com/'


async def fetch_page(session, url):
    page_start = time.time()
    async with session.get(url) as response:
        print(f'Page took {time.time() - page_start}')
        print(response.status)
        return response.status


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks


loop = asyncio.get_event_loop()
urls = [TARGET_URL for i in range(50)]

start = time.time()
loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f'All took: {time.time() - start}')
