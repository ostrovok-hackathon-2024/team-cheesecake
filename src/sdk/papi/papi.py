# https://github.com/EmergingTravel/papi-sdk-python
from papi_sdk import APIv3

from config import PAPI_LOGIN, PAPI_PASSWORD 

key = f"{PAPI_LOGIN}:{PAPI_PASSWORD}"
papi = APIv3(key=key)
