import asyncio
import time

@asyncio.coroutine
def clock(idx):
    print("Current time from asynchronous {},code: {}".format(idx, int(time.time())))
    yield from asyncio.sleep(1)


def blocking(loop):
    idx = 0
    while True:
        time.sleep(3)
        s = asyncio.async(clock(idx))
        loop.run_until_complete(asyncio.wait([s]))
        print("Current time from blocking {} code: {}".format(idx,int(time.time())))
        idx += 1


def main():
    loop = asyncio.get_event_loop()
    block = loop.run_in_executor(None, blocking, loop)
    loop.run_forever()

if __name__ == '__main__':
    main()
