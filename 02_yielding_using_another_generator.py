from collections import deque

dataset = deque(('Python', 'Ruby', 'Go', 'C', 'JS', 'Java'))

def get_data():
    # Similar as (x for x in languages)
    yield from dataset

def say_hello(gen):
    while True:
        try:
            lang = next(gen)
            yield f'Hello, {lang}!'
        except StopIteration:
            break
    print('Finish!')

languages = get_data()

g = say_hello(languages)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
