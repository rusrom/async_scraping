import aiohttp
import asyncio

# Fetching a single page
# All we need is to get the event loop and run it until it completes

# Our coroutine
async def fetch_page(url):
    # Create client session
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(response.status)
            return response.status

loop = asyncio.get_event_loop()
loop.run_until_complete(fetch_page('https://kartochki-domana.com.ua/ru/?s=%D0%BA%D0%B0&submit=Search&post_type=product'))
