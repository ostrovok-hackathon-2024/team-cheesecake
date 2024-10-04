import os 

from dotenv import load_dotenv

load_dotenv()

PAPI_LOGIN = os.environ.get("PAPI_LOGIN")
PAPI_PASSWORD = os.environ.get("PAPI_PASSWORD")
