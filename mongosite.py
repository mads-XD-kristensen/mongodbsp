# Sitet printer ikke alt datene fra db men det gør den i terminalen
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/")
def hello():
    items = get_items
    return f"<p>{items}</p>"

def get_database():
    CONNECTION_STRING  = "mongodb://localhost:27017/"
    client = MongoClient(CONNECTION_STRING)
    return client['twitter']

def get_items():
    dbname = get_database()
    collection_name = dbname["tweets"]
 
    item_details = collection_name.find()
    for item in item_details:
        print(item)
    return item_details
    
get_items()