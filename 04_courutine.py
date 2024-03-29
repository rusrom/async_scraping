from collections import deque


target_urls = deque(
    (
        'https://www.PYTHON.org/1',
        'https://www.PYTHON.org/2',
        'https://www.PYTHON.org/3',
        'https://www.PYTHON.org/4',
        'https://www.PYTHON.org/5',
    )
)


# COROUTINE
def scrape_resources():
    '''Generator recieving data no longer called gnrrator.
    Because it not generating anything.
    It recieve data and can be suspended while do something with it!
    Such type of generators known as COROUTINES.
    '''
    while target_urls:
        target_url = target_urls.popleft().lower()
        message = yield  # <= task.send(message) (2)
        print(f'{message}: {target_url}')


def start(task):
    # task.send(None)
    # while True:
    #     message = yield  # <= greeter.send('Hello') (1)
    #     task.send(message)
    
    # ALL COMMENTED CODE ABOVE IS EQUVIVALENT TO:
    yield from task
    # Nobody understood: yield from)
    # So a new keyword was invented in order to get rid of yield from
    # This keyword is called AWAIT

task = scrape_resources()
work = start(task)
work.send(None)

work.send('Getting target 1')  # (0)
print('Some music is playing...')

work.send('Getting target 2')
print('Knock, knock')

work.send('Getting target 3')
print('Cup of tea')
