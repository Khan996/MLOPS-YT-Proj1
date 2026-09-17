import os 
import sys
import pymongo 
import certifi

from src.exception import MyException 
from src.logger import logging 
from src.constants import DATABASE_NAME, MONGODB_URL_KEY

# Load the certificate authority file to avoid timeout errors when connecting to MongoDB 
ca = certifi.where()

class MongoDBClient:
    """
    MongoDBClient is responsible for establishing a connection to database.
    
    Attribute:
    ----------
    client: MongoClient
        A shared Mongo instance for class 
    database: Database
        The specific databse instance that Mongo connects to.
        
    Methods:
    --------
    __init__(databse_name: str) --> None:
    
    Initializes the MongoDB connection using the give database name. 

    """

    client = None  # Shared MongoClient across all MongoDBClient instances 

    def __init__(self, database_name: str = DATABASE_NAME) -> None:
        """
        Initialize a connection to MongoDB database. If no connection is found, it establishes a new one. 

        Parameters:
        -----------

        database_name : str, optional 
            Name of the MongoDB database connects to. Default is set by DATABASE_NAME constant. 

        Raises:
        -------
        MyException
            If there is an issue connecting to MongoDB or if the environment variable for the MongoDB URL is not set. 

        """

        try:
            # check if MongoDB connection has already been established; if not, create a new one. 
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment variable '{MONGODB_URL_KEY}' is not set.")

                # Establish a new MongoDB client connection 
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

            # Use the shared MongoCLient for this instance
            self.client = MongoDBClient.client
            self.database = self.client[database_name] # connect to the specified database
            self.database_name = database_name
            logging.info("MongoDB Connection successful.")

        except Exception as e:
            # Raise a custom exception with traceback details if connection fails
            raise MyException(e, sys)
