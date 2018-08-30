from flask import Flask, jsonify, abort, request
import requests
import json
import socket
import os
from edityaml import editYaml
import subprocess

app = Flask(__name__)

@app.route("/")
def hello():
	return "<h1>Orchestrator</h1>"

@app.route("/list_services", methods=['GET'])
def list_services():
	"""List available services"""

	data = request.args

	if data == "":
		return "400"
	else:
		nodeId=data["hostname"]
		nodeId=nodeId.encode ("ascii")
		nodeId=nodeId.lower()
		Service=data["service"]
		print "+++Request for service: %s, by: %s" % (data["service"], data["hostname"])
		editYaml("controlapp_v2_deployment.yaml","nodeAffinity", [nodeId])
		subprocess.call("kubectl apply -f controlapp_v2_deployment.yaml",shell=True)		
		return "<h2>User %s is allowed</h2>" % data["hostname"]
		
if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port=6000)

