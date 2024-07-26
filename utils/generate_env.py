import os

STATUS_DEPLOYMENT = os.getenv("STATUS_DEPLOYMENT")
MONGO_URI_DEV = os.getenv("MONGO_URI_DEV")
MONGO_URI_PROD = os.getenv("MONGO_URI_PROD")
API_MODULE_DEV = os.getenv("API_MODULE_DEV")
API_MODULE_PROD = os.getenv("API_MODULE_PROD")


def generate_env():
    body={}
    if STATUS_DEPLOYMENT == "development":
        body =  {
        "api_module": API_MODULE_DEV,
        "db_url": MONGO_URI_DEV
        }
    else:
        body =  {
            "api_module": API_MODULE_PROD,
            "db_url": MONGO_URI_PROD
        }
    return body