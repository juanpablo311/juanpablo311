from pymongo import MongoClient
uri = "mongodb+srv://myAtlasDBUser:32671422202@myatlasclusteredu.giajzog.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
for db_name in client.list_database_names():
    print (db_name)