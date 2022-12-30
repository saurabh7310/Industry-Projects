import pandas as pd 
from  sensor.config import mongo_client
from sensor.logger import logging
from sensor.exception import SensorException
import os, sys

def get_collection_as_dataframe()->pd.DataFrame:
    try:
        logging.info(f"Reading data from Database: {database_name} and collection: {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found Columns: {df.columns}")

        if "_id" in df.columns:
            df = df.drop("_id", axis=1)
        logging.info(f"Row and Columns in df: {df.shape}")
        return df 
    except Exception as e:
        SensorException(e, sys)