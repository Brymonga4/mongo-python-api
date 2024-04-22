from pymongo import MongoClient

print('Hello World!')

client = MongoClient("mongodb://root:example@mongo:27017")

if client:
    print("Conexión exitosa")

db = client.testdb

collection= db.collectiontest
documento = {"nombre": "ejemplo"}
collection.insert_one(documento)

print("Número total de documentos:", collection.count_documents({}))
result = collection.find()

print("Antes del bucle")
for document in result:
    print(document)
print("Después del bucle")

client.close()