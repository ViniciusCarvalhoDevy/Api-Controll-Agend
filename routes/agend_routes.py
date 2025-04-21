from flask import Blueprint, request
from services.agend_service import get_all_agends, get_agend_by_id, create_agend, update_agend, delete_agend,get_all_agends_with_serving,get_free_agends_for_date,get_agend_with_serving_for_id

agend_bp = Blueprint('agend', __name__)

@agend_bp.route('/', methods=['GET'])
def get_agends():
    return get_all_agends()

@agend_bp.route('/<int:agend_id>', methods=['GET'])
def get_agend(agend_id):
    return get_agend_by_id(agend_id)

@agend_bp.route('/', methods=['POST'])
def create_new_agend():
    return create_agend(request.json)

@agend_bp.route('/<int:agend_id>', methods=['PUT'])
def update_existing_agend(agend_id):
    return update_agend(agend_id, request.json)

@agend_bp.route('/<int:agend_id>', methods=['DELETE'])
def delete_existing_agend(agend_id):
    return delete_agend(agend_id)

@agend_bp.route('/agends_complete', methods=['GET'])
def get_agends_with_serving():
    return get_all_agends_with_serving()

@agend_bp.route('/agends_complete/<int:agend_id>', methods=['GET'])
def get_agends_with_serving_for_id(agend_id):
    return get_agend_with_serving_for_id(agend_id)

@agend_bp.route('/free',methods=['GET'])
def get_free_agends():
    return get_all_agend_with_serving_for_id()
