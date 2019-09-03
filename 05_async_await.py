from collections import deque
from types import coroutine


target_urls = deque(
    (
        'https://www.PYTHON.org/1',
        'https://www.PYTHON.org/2',
        'https://www.PYTHON.org/3',
        'https://www.PYTHON.org/4',
        'https://www.PYTHON.org/5',
    )
)


@coroutine
def scrape_resources():
    while target_urls:
        target_url = target_urls.popleft().lower()
        message = yield  # <= task.send(message) (2)
        print(f'{message}: {target_url}')


async def start(task):
    print('Starting...')
    await task
    print('Stopping...')

task = scrape_resources()
work = start(task)
work.send(None)

work.send('Getting target 1')  # (0)
print('Some music is playing...')

work.send('Getting target 2')
print('Knock, knock')

work.send('Getting target 3')
print('Cup of tea')

work.send('Getting target 3')
print('Cup of tea')

# Only after this operation we can see 'Stopping...' message
# Befor we just awaiting!
# work.send('Getting target 3')
# print('Cup of tea')
