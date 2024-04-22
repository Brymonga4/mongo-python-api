import mysql.connector
from mysql.connector import errorcode
import mariadb 

class MariaDBConnection:
    def __init__(self, db_name='my_mariadb', user="api_user", password="api_user", host="mariadb", port=3306):
        self.connection = None 
        try:
            self.connection = mariadb.connect(
                host=host,
                user=user,
                password=password,
                database=db_name,
                port=port
            )
            self.cursor = self.connection.cursor(dictionary=True)
            print("Conexión a MariaDB exitosa")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Usuario o contraseña equivocada")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("La base de datos no existe")
            else:
                print(err)            

    def cerrar_conexion(self):
        self.cursor.close()
        self.connection.close()
