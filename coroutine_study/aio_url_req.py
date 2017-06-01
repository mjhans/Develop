import asyncio
from aiohttp import ClientSession

@asyncio.coroutine
def hello(url):
	with ClientSession() as session:
		with session.get(url) as response:
			r = yield from response.read()
			print(r)

loop = asyncio.get_event_loop()

tasks = []

url = 'http://httpbin.org/get?{0}'
for i in range(100):
	task = asyncio.async(hello(url.format(i)))
	tasks.append(task)

loop.run_until_complete(asyncio.wait(tasks))