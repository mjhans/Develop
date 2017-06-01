import asyncio
import time


def slow_function():
    time.sleep(3)
    return 42


@asyncio.coroutine
def test1(loop):
    res = yield from loop.run_in_executor(None, slow_function)
    print(res)
    print('Finish test1')


@asyncio.coroutine
def test2():
    for i in range(0, 10):
        print(i)
        yield from asyncio.sleep(0.5)
    print('Finish test2')


loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.wait([
        test1(loop),
        test2()
    ])
)