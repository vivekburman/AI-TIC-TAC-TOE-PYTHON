from flask_restful import Resource
from flask import Flask, request
from Configs import APIConfig
import platform
class Info(Resource):
	def get(self):
		return {
			'context':"VIVEK REST API",
			'author': "VIVEK BURMAN",
			'organization': "VIVEK BURMAN",
			'os': platform.linux_distribution(),
			'kernel': platform.system() + " " + platform.release(),
			'version': APIConfig.API['version'],
			'ip_address': request.remote_addr
}
