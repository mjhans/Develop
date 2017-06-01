import timeit
import aiohttp
import asyncio

urls = ['http://shopping.naver.com/search/category.nhn?pagingIndex=1&pagingSize=40&productSet=model&viewType=list&sort=rel&cat_id=50001459&frm=NVSHMDL',
        'http://google.com', 'http://apple.com']


HEADER = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}
@asyncio.coroutine
def fetch(url):
	print('Start', url)
	req = yield from aiohttp.request('GET', url, headers=HEADER)
	print('Done', url)
	
@asyncio.coroutine
def fetch_all(urls):
	fetches = [asyncio.Task(fetch(url)) for url in urls]
	yield from asyncio.gather(*fetches)

start = timeit.default_timer()
asyncio.get_event_loop().run_until_complete(fetch_all(urls))
duration = timeit.default_timer() - start

print(duration)
