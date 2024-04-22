# factories/todo_crud_factory.py
import os
from databases.mongo.mongoCRUD import MongoTodoCRUD
from databases.maria_db.mariadbCRUD import MariaDBTodoCRUD

def get_todo_crud(database_type):
    if database_type == 'MONGO':
        return MongoTodoCRUD("tasksdb")
    elif database_type == 'MARIADB':
        return MariaDBTodoCRUD("my_mariadb")
    else:
        raise ValueError(f"No se acepta esa database {database_type}")
    
def get_user_crud(database_type):
    if database_type == 'MONGO':
        return MongoTodoCRUD("tasksdb")
    elif database_type == 'MARIADB':
        return MariaDBTodoCRUD("my_mariadb")
    else:
        raise ValueError(f"No se acepta esa database {database_type}")
