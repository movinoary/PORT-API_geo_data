from db.connection import get_database
from utils.generate_uuid import generate_uuid
from utils.generate_time import generate_time
collection = get_database()
 
def get_geo_datas(create_by):
    item_details = collection.find({"createBy": create_by})
    return list(item_details)

def get_geo_data(_id): 
    item_details = collection.find({"_id": _id})
    for item in item_details:
        return item

def add_geo_data(data): 
    try:
        body = {
            "_id":  generate_uuid(),
            "createBy": "VOSSO-3010-ALJPB-82468HW-BVZDMSDJ6O-S9CAH",
            "geoJson" : data,
            "createAt": generate_time(),
            "updateAt": generate_time()
        }
        collection.insert_one(body)
        return "success"
    except:
        return "error"

def update_geo_data(_id, data): 
    try:
        body = {
            "geoJson" : data,
            "updateAt": generate_time()
        }
        # collection.insert_one(body)
        collection.update_many({'_id': _id}, {'$set': body})
        return "success"
    except:
        return "error"

def delete_geo_data(_id):
    try:
        collection.delete_many({'_id': _id})
        return "success"
    except:
        return "error"
