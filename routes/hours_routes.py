from flask import Blueprint, request
from services.hours_service import get_all_hours, get_hour_by_id, create_hour, update_hour, delete_hour

hours_bp = Blueprint('hours', __name__)

@hours_bp.route('/', methods=['GET'])
def get_hours():
    return get_all_hours()

@hours_bp.route('/<int:hour_id>', methods=['GET'])
def get_hour(hour_id):
    return get_hour_by_id(hour_id)

@hours_bp.route('/', methods=['POST'])
def create_new_hour():
    return create_hour(request.json)

@hours_bp.route('/<int:hour_id>', methods=['PUT'])
def update_existing_hour(hour_id):
    return update_hour(hour_id, request.json)

@hours_bp.route('/<int:hour_id>', methods=['DELETE'])
def delete_existing_hour(hour_id):
    return delete_hour(hour_id)
