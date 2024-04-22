from pymongo import MongoClient

class Conection:
    def __init__ (self, user, password, host, port ):
        self.client = MongoClient(f"mongodb://{user}:{password}@{host}:{port}")

    @staticmethod
    def por_defecto(user ="root", password = "example", host = "mongo", port = "27017"):
        return Conection(user, password, host, port)
    
    def cerrar_conexion(self):
        self.client.close()
    
class ToDo:
    def __init__(self, title, date, iscomplete):
        self.title = title
        self.date = date
        self.iscomplete = iscomplete

    def to_dict(self):
        return {
            "title": self.title,
            "date": self.date,
            "iscomplete": self.iscomplete
        }

class CRUD:
    def __init__(self, ToDo, collection):
        self.ToDo = ToDo
        self.collection = collection

    def insertToDo(self, ToDo):
        documento = ToDo.to_dict()
        self.collection.insert_one(documento)
        print("Insertado")



    
conexion = Conection.por_defecto()

if conexion.client:
    print("Conexión exitosa")

db = conexion.client.testdb
collection = db.colltest

""" 
title = input("Ingrese el título del documento: ")
date = input("Ingrese la fecha (formato YYYY-MM-DD): ")
iscomplete = input("¿Está completo? (True/False): ").lower() == "true"
"""
title = "Tarea por hacer"
date = "2024-01-18"
iscomplete = False

mi_ToDo = ToDo(title, date, iscomplete)

crud = CRUD(ToDo, collection)
crud.insertToDo(mi_ToDo)

contenido = collection.find()

print("algo antes de leer los todos")

for documento in contenido:
    print(documento)

print("algo despues de leer los todos")


conexion.cerrar_conexion()