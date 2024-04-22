from dotenv import dotenv_values
from interfaces import todos_blueprint
from factories.todo_crud_factory import get_todo_crud
from interfaces import todos_blueprint, users_blueprint
from flask import Flask

ROUTES = {
    'MONGO': '/api/v1',
    'MARIADB': '/api/v2',
    'GRAPHQL': '/graphql'
}

ENV = dotenv_values()
app = Flask(__name__)

todos_bp_setup = todos_blueprint.TodoBlueprintSetup()
users_bp_setup = users_blueprint.UserBlueprintSetup()

def enableRoute(moduleName = ''):
    if moduleName == 'MONGO':
        mongo_crud = get_todo_crud('MONGO')
        configure_crud(mongo_crud, moduleName)
    elif moduleName == 'MARIADB':
        mariadb_crud = get_todo_crud('MARIADB')
        configure_crud(mariadb_crud, moduleName)
    elif moduleName == 'GRAPHQL':
        pass
            
    print(moduleName)
    return moduleName

def configure_crud(database_crud, moduleName):
    todos_bp_setup.configure_crud(database_crud)
    users_bp_setup.configure_crud(database_crud)
    todos_bp_setup.add_routes()
    users_bp_setup.add_routes()
    app.register_blueprint(todos_bp_setup.blueprint, url_prefix=ROUTES[moduleName])
    app.register_blueprint(users_bp_setup.blueprint, url_prefix=ROUTES[moduleName])

response = {}
for key, value in ROUTES.items():
    if ENV[key] == 'true':
        response[key] = value
        enableRoute(key)

print(response)

@app.route('/')
def getRoutes():
    return response


# Levantar el servicio si se ejecuta en modo App
if __name__ == "__main__":
    print("modo app")
    app.run(host='0.0.0.0', port=8086)