from flask import Blueprint, request
from services.serving_salon_service import get_all_servings, get_serving_by_id, create_serving, update_serving, delete_serving

serving_salon_bp = Blueprint('serving_salon', __name__)

@serving_salon_bp.route('/', methods=['GET'])
def get_servings():
    return get_all_servings()

@serving_salon_bp.route('/<int:serving_id>', methods=['GET'])
def get_serving(serving_id):
    return get_serving_by_id(serving_id)

@serving_salon_bp.route('/', methods=['POST'])
def create_new_serving():
    return create_serving(request.json)

@serving_salon_bp.route('/<int:serving_id>', methods=['PUT'])
def update_existing_serving(serving_id):
    return update_serving(serving_id, request.json)

@serving_salon_bp.route('/<int:serving_id>', methods=['DELETE'])
def delete_existing_serving(serving_id):
    return delete_serving(serving_id)
