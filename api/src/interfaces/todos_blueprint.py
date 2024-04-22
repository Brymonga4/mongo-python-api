from flask import Blueprint, request, jsonify, Response
from factories.todo_crud_factory import get_todo_crud

class TodoBlueprintSetup:
    def __init__(self):
        self.todo_crud = None
        self.blueprint = Blueprint('api_rest_bp', __name__)

    def configure_crud(self, todo_crud):
        self.todo_crud = todo_crud

    def add_routes(self):
        @self.blueprint.route('/todos', methods=['POST'])
        def create_todo():
            todo_data = request.json
            try:
                new_todo_id = self.todo_crud.create(todo_data)
                return jsonify({"id": new_todo_id}), 201
            except Exception as e:
                return jsonify({"error": str(e)}), 400

        @self.blueprint.route('/todos/<todo_id>', methods=['GET'])
        def get_todo(todo_id):
            try:
                todo = self.todo_crud.read(todo_id)
                if todo:
                    todo['_id'] = str(todo['_id'])
                    print("intentando serializar")
                    return jsonify(todo)
                else:
                    return Response(status=404)
            except Exception as e:
                return jsonify({"error": str(e)}), 400

        @self.blueprint.route('/todos/<todo_id>', methods=['PUT'])
        def update_todo(todo_id):
            todo_data = request.json
            try:
                if self.todo_crud.update(todo_id, todo_data):
                    return Response(status=204)
                else:
                    return Response(status=404)
            except Exception as e:
                return jsonify({"error": str(e)}), 400

        @self.blueprint.route('/todos/<todo_id>', methods=['DELETE'])
        def delete_todo(todo_id):
            try:
                if self.todo_crud.delete(todo_id):
                    return Response(status=204)
                else:
                    return Response(status=404)
            except Exception as e:
                return jsonify({"error": str(e)}), 400


        @self.blueprint.route('/todos/user/<user_id>', methods=['GET'])
        def get_todos_by_user_id(user_id):
            if not user_id:
                return jsonify({"error": "Se necesita el parametrode user_id"}), 400

            try:
                todos = self.todo_crud.read_by_user_id(user_id)
                if todos:
                    for todo in todos:
                        todo['_id'] = str(todo['_id'])
                    return jsonify(todos)
                else:
                    return Response(status=404)
            except Exception as e:
                return jsonify({"error": str(e)}), 400
            

