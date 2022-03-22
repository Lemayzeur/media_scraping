import requests
import random
import pandas as pd
from bs4 import BeautifulSoup as bs


#Url for the list of proxy

free_proxy_url = 'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt' # TODO

# get the proxy as http response
# TODO

response_proxy = requests.get(free_proxy_url)

# Convert the http response to list of proxy
# TODO
proxy_list = response_proxy.text.strip().split("\n")


print(proxy_list)

"""

def get_random_proxy(array):
	''' get a random proxy '''
	proxy = random.choice(array)

	# to get more info on the proxy format
	# More info, visit: https://docs.python-requests.org/en/latest/api/#module-requests
	return # {'protocol': 'ip:port'} # TODO

def get_working_proxy():
	''' test random proxies, to get one that works'''
	TOTAL_TESTS = 20
	for _ in range(TOTAL_TESTS):
		proxy = get_random_proxy(<proxy_list>) # TODO
		try:
			requests.get('<test_url>', proxies=proxy) # TODO
			# if it works, return it
			return proxy
		except Exception as error:
			print(error)


# set a custom header
headers = {
	'User-Agent': '<browser>' # TODO
}

# call and get the proxy
proxy = get_working_proxy()
if proxy:

	# hit the target site
	res = requests.get('<target_site>', headers=headers, proxies=proxy) # TODO

	# init the beautiful instance as html parser
	soup = bs(<target_content> , '<parser>') # TODO

	# After collecting the data needed, convert it to pandas dataframe
  # TODO

	# then export it as csv
	df.to_csv('<path/file_name>') # TODO
else:
	print('No working proxy found. Go buy some instead')

"""