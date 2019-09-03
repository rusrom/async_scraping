# Example of multitasking using Generators
def countdown(n):
    while n > 0:
        yield n
        n -= 1

tasks = [countdown(10), countdown(5), countdown(20)]

while tasks:
	task = tasks.pop(0)
	try:
		print(next(task))
		tasks.append(task)
	except StopIteration:
		print('Task finished')
