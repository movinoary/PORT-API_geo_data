from flask import jsonify

def res_success(data):
    return jsonify({'status':200,'message': "Success", 'data': data}), 200

def res_error():
    return jsonify({'status':400,'message': "Error"}), 400

def res_failed_signature():
    return jsonify({'status':400,'message': "Failed Signature"}), 400
    