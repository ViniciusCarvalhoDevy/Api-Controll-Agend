from flask import Blueprint, request
from services.agend_serving_service import create_agend_service_salon

agend_serving_salon_bp = Blueprint('agend_serving_salon', __name__)

@agend_serving_salon_bp.route('/', methods=['POST'])
def add_new_serving_agend():
    return create_agend_service_salon(request.json)

