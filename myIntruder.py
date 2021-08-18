import requests
import concurrent.futures
import re

def getPayload():
	payloads = []
	with open("./gyapu.txt", "r") as f:
		payloads = f.read().split('\n')

	return payloads

def sendGetRequest(domain, index, payload):
	parameters = {}
	headers = {}
	cookies = {}

	domain += payload
	r = requests.get(domain, cookies=cookies)
	return r

payloads = getPayload()
domain = 'https://www.gyapu.com/'
password = ''

def sendIt(payload, index):
	response = sendGetRequest(domain, index, payload)
	match = response.text
	if response.length != 5662:
		print('Found for dir:',payload)
		return payload
	else:
		return None

i = 1
found = True

threads = []

with concurrent.futures.ThreadPoolExecutor() as executor:
	threads = [executor.submit(sendIt, payload, i) for payload in payloads]

	found = False
	for f in concurrent.futures.as_completed(threads):
		if f.result() != None:
			password+=f.result()
			found = True
			i+=1

print("Found:", found)
print('Operation Complete')