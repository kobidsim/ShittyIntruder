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
domain = 'https://www.youtube.com/'
for payload in payloads:
	response = sendGetRequest(domain, payload)
	if response.status_code == 200:
		print(payload, response.status_code, response.length)