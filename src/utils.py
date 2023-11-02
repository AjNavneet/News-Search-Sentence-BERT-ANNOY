# Import necessary libraries
from pymongo import MongoClient
import pandas as pd
import numpy as np
import os
import re
import json
import logging
import datetime

# Try importing the 'config' module, if it fails, import 'config' from the current directory
try:
    from src import config
except:
    import config

# Set up logging based on the environment
if config.ENV == "dev":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
else:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename=f"{config.LOGS_DIR}/{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.log",
        filemode='w'
    )
logger = logging.getLogger(__name__)

# Create directories for data storage and logging
os.makedirs(os.path.join(config.DATA_DIR, "raw"), exist_ok=True)
os.makedirs(os.path.join(config.DATA_DIR, "processed"), exist_ok=True)
os.makedirs(config.LOGS_DIR, exist_ok=True)
os.makedirs(config.MODELS_DIR, exist_ok=True)
os.makedirs(config.RESULTS_DIR, exist_ok=True)

# Define a function to save data as a JSON file
def save_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

# Define a function to load JSON data from a file
def load_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

# Define a function to load article lookup data
def load_article_lookup() -> dict:
    """
    Load article lookup
    :return: dict
    """
    df = pd.read_csv("data/raw/raw.csv")
    df = df[["article_id", "title", "text", "category", "subcategory"]]
    df.index = df.article_id
    df = df[["title", "text", "category", "subcategory"]].drop_duplicates()
    return df.to_dict(orient="index")

# Define a function to get raw data from AWS MongoDB
def get_raw_data_from_aws_mongo(output_filename=os.path.join(config.DATA_DIR, "raw", "raw.csv")) -> str:
    """
    Get raw data from AWS MongoDB
    :param output_filename: str
    :return: path
    """
    logger.info("Getting raw data from AWS MongoDB")
    conn = MongoClient(config.CONNECTION_STRING)
    db = conn.get_database("NewsArticleDB")
    collection = db.get_collection("news_data")
    data = pd.DataFrame(list(collection.find())).drop("_id", axis=1)
    _columns = list(map(lambda x: x.lower(), data.columns))
    data.columns = _columns

    # Remove articles with no titles and no text body
    data = data[(~data['title'].isnull()) & (~data['text'].isnull())]
    data["category"] = data["category"].apply(lambda x: x.lower())
    data["subcategory"] = data["subcategory"].apply(lambda x: x.lower())
    data["article_id"] = list(range(data.shape[0]))
    data[["article_id"] + _columns].to_csv(output_filename, index=False)
    return output_filename
