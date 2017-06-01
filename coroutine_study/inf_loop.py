import asyncio
import time
from datetime import datetime

def inf_loop():
	p_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	while True:
		show_many(p_list)
		time.sleep(1)
		


def show_many(p_list):
	loop = asyncio.get_event_loop()
	to_do = [show_one(pl) for pl in p_list]
	wait_coro = asyncio.wait(to_do)
	res, _ = loop.run_until_complete(wait_coro)
	loop.run_forever()
	


@asyncio.coroutine
def show_one(item):
	print("item: {0}, time:{1}".format(item, datetime.now()))
	

if __name__ == "__main__":
	try:
		inf_loop()
	except Exception as msg:
		print(msg)