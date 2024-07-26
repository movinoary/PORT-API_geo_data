from pymongo import MongoClient
from utils.generate_env  import generate_env

def get_database():
   db_url = generate_env()["db_url"]
   db = MongoClient(db_url)
   collection = db['geoData']["geoJSON"]
   return collection
  
if __name__ == "__main__":   
     dbname = get_database()