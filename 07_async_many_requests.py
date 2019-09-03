import aiohttp
import asyncio
import time


# Fetching a single page
# More then 1 request
# TARGET_URL = 'https://kartochki-domana.com.ua/ru/?s=%D0%BA%D0%B0&submit=Search&post_type=product'
# TARGET_URL = 'https://kartochki-domana.com.ua/'
TARGET_URL = 'http://clevertoys.com.ua/'
# TARGET_URL = 'https://google.com'

# Our coroutine
async def fetch_page(url):
    # Create client session
    page_start = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f'Page took {time.time() - page_start}')
            return response.status


loop = asyncio.get_event_loop()
tasks = [fetch_page(TARGET_URL) for i in range(30)]

# Function that collects a bunch of tasks together and run them as a single task: asyncio.gather()

# loop.run_until_complete(asyncio.gather(tasks[0], tasks[1], tasks[2]))
loop.run_until_complete(asyncio.gather(*tasks))
