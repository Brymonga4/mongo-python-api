from flask import Blueprint, request

api_rest_bp = Blueprint('api_rest_bp', __name__)

@api_rest_bp.route('/notes')
def notes():
    return { "notes": "ok" }