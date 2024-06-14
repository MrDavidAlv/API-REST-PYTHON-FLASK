from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from services import register_user, authenticate_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    return jsonify(*register_user(data))

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = authenticate_user(data)
    if isinstance(user, dict):  # Si es un dict, es un mensaje de error
        return jsonify(user), 400
    access_token = create_access_token(identity=user.id_usuario)
    return jsonify(access_token=access_token), 200
