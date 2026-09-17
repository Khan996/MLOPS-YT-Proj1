import os 
import sys
import pandas as pd
import numpy as np
from typing import Optional

from src.configuration.mongo_db_connection import MongoDBClient
from src.constants import DATABASE_NAME
from src.exception import MyException

class Proj1Data:

    """
    A class to import MongoDB records as a pandas Dataframe

    """

    def __init__(self) -> None:
        """ 
        Initializes MongoDB client connection
        
        """
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise MyException(e, sys)

    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str]=None) -> pd.DataFrame:
        """
        Exports an entire MongoDB collection as an entire DataFrame.

        Parameter:
        ----------
        collection_name: str
            The name of MongoDB Collection to export.
        database_name: Optiona[Str]
            Name of the database (optional). Defaults to DATABASE_NAME
        """
        try:
            # Access specified collection from the default or dpecified database. 
            if database_name is None: 
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]


            # convert collection data to dataframe and preprocess
            print("Fetching data from mongoDB")
            df = pd.DataFrame(list(collection.find()))
            print(f"Data fetched with len: {len(df)}")
            if "id" in df.columns.to_list():
                df = df.drop(columns=["id"])
            df.replace({"na": np.nan}, inplace=True)
            return df 

        except Exception as e:
            raise MyException(e, sys)

