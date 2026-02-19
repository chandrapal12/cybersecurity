from pymongo.mongo_client import MongoClient

URL = "mongodb+srv://<db-username>:<db-password>@cluster0.ha4wdg1.mongodb.net/?appName=Cluster0"


# create a new client and connect to the server

client = MongoClient(URL)

# check whether successfull connection or not

try:
    client.admin.command('ping')
    print("Success!")
except Exception as e:
    print(e)