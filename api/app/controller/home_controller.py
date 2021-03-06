from flask import request, escape
from flask_restplus import Resource, Namespace, fields

import sys
sys.path.append("..")

from utils.ApiResponse import ApiResponse

api = Namespace('Home', description='Basic health operations')

@api.route(
    '', 
    doc={"description": "Just to check if everything's up and running"}
)
class Home(Resource):
    def get(self):
        apiResponse = ApiResponse()
        apiResponse.setAll(False, "Everything's up and running", {})
        return apiResponse.getResponse()