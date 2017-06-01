import threading
import queue
import requests
import timeit

thread_num = 10

@profile
def doWork():
	while True:
		print(threading.current_thread().name)
		url = q.get()
		print(threading.current_thread().name,url)
		r = requests.get(url)
		print(threading.current_thread().name,r.status_code)
		q.task_done()

start = timeit.default_timer()

q = queue.Queue(thread_num)

for i in range(thread_num):
	t = threading.Thread(target=doWork)
	t.daemon = True
	t.start()

for i in range(thread_num):
	q.put('http://httpbin.org/get?key=' + str(i))

q.join()
duration = timeit.default_timer() - start
print(duration)