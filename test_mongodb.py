from pymongo import MongoClient
uri = "mongodb+srv://masteradil06_db_user:<@password>@cluster0.tfygjwd.mongodb.net/?appName=Cluster0"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)