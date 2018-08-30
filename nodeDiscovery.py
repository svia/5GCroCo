from flask import Flask, jsonify, abort, request
import requests
import json
import socket
import os

SERVICES = {"DRIVE": True,}
HOST = str(socket.gethostname())
ORCH_LIST = "http://10.1.2.151:6000/list_services"

def checkAvailableServices(service_data):
	"""Checks whether a service is available or not"""

	if str(service_data["service"][0]) in SERVICES.keys():
		specs = service_data
		specs.setdefault("hostname", HOST)
		try:
			r = requests.get(ORCH_LIST, params=specs)
			print  "%s" % r.url
		except:
			print "***>ORCH connection error"
			return False

		if (r.ok):
			print "+++>Service spawned"
			print "%s" % r.text
		else:
			print "***>ORCH API error: %s" % r.text
			return False
		return SERVICES[service_data["service"][0]]
	else:
		return False

app = Flask(__name__)

@app.route("/")
def hello():
	return "<h1>Discovery</h1>"

@app.route("/list_services", methods=['GET'])
def list_services():
	"""List available services"""

	return "%s" % json.dumps(SERVICES)

@app.route("/service_request", methods=['GET'])
def service_request():
	"""Check is requested service exists and returns this information"""
	
	data = dict(request.args)

	if data == "":
		print "<h2>You have to provide a valid service JSON structure</h2>"
		return "400"
	else:
		available = checkAvailableServices(data)
		if available is True:
			return "<h2>Service %s is available</h2>" % data["service"][0]
		else:
			return "<h2>Service %s is not available</h2>" % str(data["service"][0])
	
if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port=6000)

