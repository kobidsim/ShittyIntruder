import requests
import threading

def getPayload():
	payloads = []
	with open("./payload.txt", "r") as f:
		payloads = f.read().split('\n')

	return payloads

def sendGetRequest(domain, payload):
	parameters = {'search': '<' + payload + '>'}
	headers = {}
	cookies = {}

	r = requests.get(domain, params=parameters, headers=headers, cookies=cookies)
	return r

payloads = getPayload()
domain = 'https://ac091fe61f7388628064ac9700900030.web-security-academy.net/'

def sendIt(payload):
	response = sendGetRequest(domain, payload)
	if response.status_code == 200:
		print(payload, response.status_code)

threads = []

for payload in payloads:
	t = threading.Thread(target=sendIt, args=[payload])
	threads.append(t)

for t in threads:
	t.start()

for t in threads:
	t.join()

print('Success')