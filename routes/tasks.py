from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services import create_task, get_user_tasks

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['POST'])
@jwt_required()
def create_task_route():
    data = request.get_json()
    current_user_id = get_jwt_identity()
    return jsonify(*create_task(data, current_user_id))

@tasks_bp.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks_route():
    current_user_id = get_jwt_identity()
    tasks = get_user_tasks(current_user_id)
    return jsonify(tasks), 200
