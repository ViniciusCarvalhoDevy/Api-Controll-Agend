from flask import Blueprint, request
from services.serving_salon_serving import get_all_servings, get_serving_by_id, create_serving, update_serving, delete_serving

agend_serving_salon_bp = Blueprint('agend_serving_salon', __name__)

@agend_agend_serving_salon_bp.route('/', methods=['POST'])
def add_new_serving_agend():
    return add_new_serving_agend(request.json)

