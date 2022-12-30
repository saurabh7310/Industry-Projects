import pymongo
import pandas as pd  
import json 
import os

@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")
    aws_access_key_id:str = os.getenv("AWS_ACCESS_KEY_ID")
    aws_access_secret_key

env_var = EnvironmentVariable()


mongo_client = pymongo.Mongoclient(env_var.mongo_db_url)