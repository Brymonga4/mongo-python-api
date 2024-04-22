from .db_connection import Connection
from bson import ObjectId
from entities import todo, user
from interfaces.CRUDInterface import CRUDInterface
from datetime import datetime

class MongoTodoCRUD(CRUDInterface):
    def __init__(self, db_name):
        self.connection = Connection(db_name)
        self.collection = self.connection.db.todos

    def create(self, todo_data):
        if 'created_date' in todo_data and isinstance(todo_data['created_date'], str):
                todo_data['created_date'] = datetime.fromisoformat(todo_data['created_date'])
        if 'last_update_date' in todo_data and isinstance(todo_data['last_update_date'], str):
            todo_data['last_update_date'] = datetime.fromisoformat(todo_data['last_update_date'])
        result = self.collection.insert_one(todo_data)
         # Devuelve id insertada
        return str(result.inserted_id)

    def read(self, todo_id):
        todo = self.collection.find_one({"_id": ObjectId(todo_id)})
        if todo:
            return todo
        return None

    def update(self, todo_id, update_data):
        result = self.collection.update_one({"_id": ObjectId(todo_id)}, {"$set": update_data})
        return result.modified_count

    def delete(self, todo_id):
        result = self.collection.delete_one({"_id": ObjectId(todo_id)})
        return result.deleted_count
    
    def read_by_user_id(self, user_id):
        result = list(self.collection.find({"user_id": user_id}))
        if result:
            return result 
        return None



    
class MongoUserCRUD(CRUDInterface):
    def __init__(self, db_name):
        self.connection = Connection(db_name)
        self.collection = self.connection.db.users

    def create(self, user_data):
        result = self.collection.insert_one(user_data)
        return str(result.inserted_id)

    def read(self, user_id):
        user = self.collection.find_one({"id": user_id})
        if user:
            return user
        return None

    def update(self, user_id, update_data):
        result = self.collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
        return result.modified_count

    def delete(self, user_id):
        result = self.collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count
        