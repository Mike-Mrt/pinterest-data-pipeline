import yaml
import requests
from time import sleep
import random
from multiprocessing import Process
import boto3
import json
import sqlalchemy
from sqlalchemy import text


random.seed(100)


class AWSDBConnector:

    # the read_db_creds() method will read the credentials yaml file and return the dictionary of the credentials
    def read_db_creds(self):
        with open('db_creds.yaml') as f:
            self.credentials = yaml.safe_load(f)

    def __init__(self):
        self.read_db_creds()
        self.HOST = self.credentials['HOST']
        self.USER = self.credentials['USER']
        self.PASSWORD = self.credentials['PASSWORD']
        self.DATABASE = self.credentials['DATABASE']
        self.PORT = self.credentials['PORT']
        
    def create_db_connector(self):
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}?charset=utf8mb4")
        return engine
            