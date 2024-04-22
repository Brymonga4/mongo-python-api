
from interfaces.CRUDInterface import CRUDInterface
from datetime import datetime
from entities import todo, user
from .db_connection import MariaDBConnection

class MariaDBTodoCRUD(CRUDInterface):
    def __init__(self, db_name='my_mariadb', user="root", password="root_password", host="mariadb", port=3306):
        self.db_connection = MariaDBConnection(db_name, user, password, host, port)
        self.cursor = self.db_connection.connection.cursor(dictionary=True)

    def create(self, todo_data):
        query = "INSERT INTO todos (title, created_date, last_update_date, is_complete, important) VALUES (%s, %s, %s, %s, %s)"
        values = (todo_data['title'], todo_data['created_date'], todo_data['last_update_date'], todo_data['is_complete'], todo_data['important'])
        self.cursor.execute(query, values)
        self.db_connection.connection.commit()
        return self.cursor.lastrowid

    def read(self, todo_id):
        query = "SELECT * FROM todos WHERE id = %s"
        self.cursor.execute(query, (todo_id,))
        todo = self.cursor.fetchone()

        if todo:
            if isinstance(todo['created_date'], str):
                todo['created_date'] = datetime.strptime(todo['created_date'], '%Y-%m-%d %H:%M:%S')
            if isinstance(todo['last_update_date'], str):
                todo['last_update_date'] = datetime.strptime(todo['last_update_date'], '%Y-%m-%d %H:%M:%S')

            new_todo = todo(
                user_id=todo['user_id'],
                title=todo['title'],
                created_date=todo['created_date'],
                last_update_date=todo['last_update_date'],
                is_complete=todo['is_complete'],
                important=todo['important']
            )
            return new_todo
        return None
    
    def update(self, todo_id, update_data):
        columns = ', '.join(f"{key} = %s" for key in update_data.keys())
        values = tuple(update_data.values()) + (todo_id,)
        query = f"UPDATE todos SET {columns} WHERE id = %s"
        self.cursor.execute(query, values)
        self.db_connection.connection.commit()
        return self.cursor.rowcount

    def delete(self, todo_id):
        query = "DELETE FROM todos WHERE id = %s"
        self.cursor.execute(query, (todo_id,))
        self.db_connection.connection.commit()
        return self.cursor.rowcount
    
class MariaDBUserCRUD(CRUDInterface):
    def __init__(self, db_name='my_mariadb', user="api_user", password="api_user", host="localhost", port=3306):
        self.db_connection = MariaDBConnection(db_name, user, password, host, port)
        self.cursor = self.db_connection.connection.cursor(dictionary=True)

    def create(self, user_data):
        query = "INSERT INTO users (username, pwd) VALUES (%s, %s)"
        values = (user_data['username'], user_data['pwd'])
        self.cursor.execute(query, values)
        self.connection.commit()
        return self.cursor.lastrowid

    def read(self, user_id):
        query = "SELECT * FROM users WHERE id = %s"
        self.cursor.execute(query, (user_id,))
        user = self.cursor.fetchone()

        if user:
            new_user = user(id=user['id'], username=user['username'], pwd=user['pwd'])
            return new_user
        return None

    def update(self, user_id, update_data):
        columns = ', '.join(f"{key} = %s" for key in update_data.keys())
        values = tuple(update_data.values()) + (user_id,)
        query = f"UPDATE users SET {columns} WHERE id = %s"
        self.cursor.execute(query, values)
        self.connection.commit()
        return self.cursor.rowcount

    def delete(self, user_id):
        query = "DELETE FROM users WHERE id = %s"
        self.cursor.execute(query, (user_id,))
        self.connection.commit()
        return self.cursor.rowcount

    def cerrar_conexion(self):
        self.cursor.close()
        self.connection.close()    