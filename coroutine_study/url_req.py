import requests
import timeit

url_basis = 'http://httpbin.org/get?'
start = timeit.default_timer()

for i in range(100):
	url = url_basis + str(i)
	print('Start', url)
	r = requests.get(url)
	print('Done', url)

duration = timeit.default_timer()-start

print(duration)