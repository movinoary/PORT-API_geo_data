from flask import Flask, request
from lib.action import get_geo_datas, get_geo_data, add_geo_data, update_geo_data, delete_geo_data
from lib.response import res_error, res_failed_signature, res_success
from lib.protect import protect_decode
from utils.generate_request import generate_request

app = Flask(__name__)
path = '/api/v1'

@app.route("/")
def home():
    return "WELCOME TO VO GEO SERVER"

@app.route(f"{path}/geo-data")
def get_datas():
    req=generate_request(request)
    protecRoute=protect_decode()
    if protecRoute == False:
        return res_failed_signature()
    
    data = get_geo_datas(req['create_by'])
    return res_success(data)

@app.route(f"{path}/geo-data/<string:_id>")
def get_data(_id):
    protecRoute=protect_decode()
    if protecRoute == False:
        return res_failed_signature()
    
    data = get_geo_data(_id)
    return res_success(data)

@app.route(f"{path}/add-data", methods=['POST'])
def add_data():
    # protecRoute=protect_decode()
    # if protecRoute == False:
    #     return res_failed_signature()
    
    data = add_geo_data(request.json)
    if(data == "success"): 
        return res_success(request.json)
    else: 
        return res_error()

@app.route(f"{path}/update-data/<string:_id>", methods=['PUT'])
def update_data(_id):
    protecRoute=protect_decode()
    if protecRoute == False:
        return res_failed_signature()
    
    data = update_geo_data(_id, request.json)
    if(data == "success"): 
        return res_success(f"Success update data in id:{_id}")
    else: 
        return res_error()

@app.route(f"{path}/delete-data/<string:_id>", methods=['DELETE'])
def delete_data(_id):
    protecRoute=protect_decode()
    if protecRoute == False:
        return res_failed_signature()
    
    data = delete_geo_data(_id)
    if(data == "success"): 
        return res_success(f"delete data in id:{_id}")
    else: 
        return res_error()
