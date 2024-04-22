from pymongo import MongoClient

class Connection:
    def __init__ (self, db_name='mongodb', user ="root", password = "example", host = "mongo", port = "27017" ):
        self.client = MongoClient(f"mongodb://{user}:{password}@{host}:{port}")
        self.db = self.client[db_name]
        self.todos_collection = self.db.todos

    def cerrar_conexion(self):
        self.client.close()