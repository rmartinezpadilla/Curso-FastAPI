from pymongo import MongoClient

# Base de datos local
#db_client = MongoClient().Ejercicio

# Base de datos remota
db_client = MongoClient(
                        "mongodb+srv://rubenmartinez:test009@cluster0.gaq5mqh.mongodb.net/?retryWrites=true&w=majority"
                        ).EJERCICIO