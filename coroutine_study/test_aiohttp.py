#!/usr/bin/env python
#coding=utf8

import asyncio
import aiohttp

from coroutine_study.flags import BASE_URL, save_flag, show, main

@asyncio.coroutine
def get_flag(cc):
	url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
	print(url)
	resp = yield from aiohttp.request('GET', url)
	img = yield from resp.text()
	return img

@asyncio.coroutine
def download_one(cc):
	img = yield from get_flag(cc)
	show(cc)
	print(img)
	#save_flag(img, cc.lower() + '.gif')
	return cc

def download_many(cc_list):
	loop = asyncio.get_event_loop()
	to_do = [download_one(cc) for cc in sorted(cc_list)]
	wait_coro = asyncio.wait(to_do)
	print(wait_coro)
	res, _ = loop.run_until_complete(wait_coro)
	
	loop.close()
	
	return len(res)

if __name__ == '__main__':
	try:
		main(download_many)
	except Exception as msg:
		print(msg)