import requests
from utils.generate_env  import generate_env

def generate_uuid():
    url = f"{generate_env()['api_module']}/uuid/geo"
    response = requests.post(url)
    return response.json()['data']

