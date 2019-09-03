def add_url():
    '''Suspend the function but then also recieve a value after we resume it.
    And the value we recieved is gouing to friend variable.
    '''
    target_url = yield
    print(f'Target URL:, {target_url}')

g = add_url()

# Priming the generator
g.send(None)
g.send('https://realpython.com/')
