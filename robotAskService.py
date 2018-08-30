import requests
import json
import socket
import time

# CONSTANTS
IP_ADD = "2.1.2.1"
URL = "http://10.1.2.153:6000/service_request"
# /CONSTANTS


def send_to_API(data):
	"""Sends the request r to the API"""
	
	try:
		r = requests.get(URL, params=data)
	except:
		print "***> Connection error"
		return

	if (r.ok):
		print "+++> Service request sent"
		print "%s" % r.text
	else:
		print "***> API error: %s" % r.text

def main():

	time.sleep(20)

	query = {}
	query.setdefault("robotIp", IP_ADD)
	query.setdefault("robotId", "Robot1")
	query.setdefault("service", "DRIVE")

	print "--->Sending request of:"
	for k,v in query.items():
		print "%s: %s" % (k,v)

	send_to_API(query)


if __name__ == '__main__':
	main()

