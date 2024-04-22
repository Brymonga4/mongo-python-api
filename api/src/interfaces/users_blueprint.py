from flask import Blueprint, request, jsonify, Response
from factories.todo_crud_factory import get_user_crud 

class UserBlueprintSetup:
    def __init__(self):
        self.user_crud = None
        self.blueprint = Blueprint('api_user_bp', __name__)

    def configure_crud(self, user_crud):
        self.user_crud = user_crud

    def add_routes(self):
        @self.blueprint.route('/users', methods=['POST'])
        def create_user():
            user_data = request.json
            try:
                new_user_id = self.user_crud.create(user_data)
                return jsonify({"id": new_user_id}), 201
            except Exception as e:
                return jsonify({"error": str(e)}), 400

        @self.blueprint.route('/users/<user_id>', methods=['GET'])
        def get_user(user_id):
            try:
                user = self.user_crud.read(user_id)
                if user:
                    user['id'] = str(user['id'])
                    return jsonify(user)
                else:
                    return Response(status=404)
            except Exception as e:
                return jsonify({"error": str(e)}), 400

        @self.blueprint.route('/users/<user_id>', methods=['PUT'])
        def update_user(user_id):
            user_data = request.json
            try:
                if self.user_crud.update(user_id, user_data):
                    return Response(status=204)
                else:
                    return Response(status=404)
            except Exception as e:
                return jsonify({"error": str(e)}), 400

        @self.blueprint.route('/users/<user_id>', methods=['DELETE'])
        def delete_user(user_id):
            try:
                if self.user_crud.delete(user_id):
                    return Response(status=204)
                else:
                    return Response(status=404)
            except Exception as e:
                return jsonify({"error": str(e)}), 400
