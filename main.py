from flask import Flask,request
from flask_restful import Api, Resource, reqparse
import pandas as pd
import xlrd

app = Flask(__name__)
api = Api(app)

class Cars(Resource):
    def get(self):
        data = pd.read_excel('car.xlsx')
        data = data.to_dict('records')
        return {'data' : data}, 200
    
    def post(self):
        id = request.args['id']
        company_name = request.args['company_name']
        model_name = request.args['model_name']
        year = request.args['year']
        km = request.args['km']

        data = pd.read_excel('car.xlsx')

        new_data = pd.DataFrame({
            'id'               :[id],
            'company_name'     : [company_name],
            'model_name'       : [model_name],
            'year'             : [year],
            'km'               : [km]
        })

        data = data.append(new_data, ignore_index = True)
        data.to_excel('car.xlsx', index=False)
        return {'data' : new_data.to_dict('records')}, 200
    
    def put(self):
        id = request.args['id']
        company_name = request.args['company_name']
        model_name = request.args['model_name']
        year = request.args['year']
        km = request.args['km']
        new_data = pd.DataFrame({
            'id'               :[id],
            'company_name'     : [company_name],
            'model_name'       : [model_name],
            'year'             : [year],
            'km'               : [km]})
        
        data = pd.read_excel('car.xlsx')
        data = data.to_dict('records')
        for new_data in data:
            if  new_data['id'] == id:
                new_data['company_name'] == company_name
                new_data['model_name'] == model_name
                new_data['year'] == year
                new_data['km'] == km
        
        data.append(new_data)
        #data = data.append(new_data, ignore_index = True)
        # data.to_excel('car.xlsx', index=False)
        return {'data' : new_data}, 200
    def delete(self):
        name = request.args['company_name']
        data = pd.read_excel('car.xlsx')
        data = data[data['company_name'] != name]
        data.to_excel('car.xlsx', index=False)
        return {'message' : 'Record deleted successfully.'}, 200

class Id(Resource):
    def get(self):
        data = pd.read_excel('car.xlsx',usecols=[0])
        data = data.to_dict('records')
        
        return {'data' : data}, 200

class Company_Name(Resource):
    def get(self,name):
        data = pd.read_excel('car.xlsx')
        data = data.to_dict('records')
        for entry in data:
            if entry['company_name'] == name :
                return {'data' : entry}, 200
        return {'message' : 'No entry found with this name !'}, 404


api.add_resource(Cars, '/car')
api.add_resource(Id, '/id')
api.add_resource(Company_Name, '/<string:name>')

if __name__ == '__main__':
    app.run(host="localhost", port=5000)
    app.run()