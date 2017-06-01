import asyncio
import aiohttp
import json

@asyncio.coroutine
def get(url):
	response = yield from aiohttp.request('GET', url)
	html = yield from response.text()
	print(type(html))
	return html


@asyncio.coroutine
def connect_one(idx):
	url = 'http://httpbin.org/get?key={0}'.format(idx)
	text = yield from get(url)
	obj = json.loads(text)
	print(type(obj))
	return obj
	
def connect_many(idx_list):
	loop = asyncio.get_event_loop()
	to_do = [connect_one(idx) for idx in idx_list]
	wait_coro = asyncio.as_completed(to_do)
	#wait_coro = asyncio.wait(to_do)
	for co in wait_coro:
		res = yield from co
		print(res)
	res, _ = loop.run_until_complete(wait_coro)
	loop.close()
	
	return res
	

def main(connect_many):
	#connect_many(range(100))
	ret = connect_many([1,2,3,4,5,6,7,8,9,10])
	print("return :  {0}".format(ret))
	
if __name__ == "__main__":
	try:
		main(connect_many)
	except Exception as msg:
		print(msg)