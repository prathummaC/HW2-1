from flask import Flask , request
from flask_restful import Resource , Api,reqparse
import json ,time 

app = Flask (__name__)
api = Api(app) 

parser = reqparse.RequestParser()
parser.add_argument('birthday')

class Age(Resource):
	def post(self): 
		args = parser.parse_args()
		bd = args['birthday']
		days,months,years = bd.split('-')
		
		Ages = int(time.strftime("%Y")) - int(years)
		
		if int(months)>int(time.strftime("%m")):
			Ages-=1
		if int(months)==int(time.strftime("%m")):
			if int(time.strftime("%d"))<int(days):
				Ages-=1
		return {"birthdate":birthday, "age":Ages}

api.add_resource(Age,'/age')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5500)
