from flask import Blueprint, request
from services.employee_service import get_all_employees, get_employee_by_id, create_employee, update_employee, delete_employee,send_encrypted_key,update_password_employee,desactive_employee

employee_bp = Blueprint('employee', __name__)

@employee_bp.route('/', methods=['GET'])
def get_employees():
    return get_all_employees()

@employee_bp.route('/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    return get_employee_by_id(employee_id)

@employee_bp.route('/', methods=['POST'])
def create_new_employee():
    return create_employee(request.json)

@employee_bp.route('/<int:employee_id>', methods=['PUT'])
def update_existing_employee(employee_id):
    return update_employee(employee_id, request.json)

@employee_bp.route('/pass/<int:employee_id>', methods=['PUT'])
def update_password_employee(employee_id):
    return update_password_employee(employee_id, request.json)

@employee_bp.route('/actv/<int:employee_id>', methods=['PUT'])
def desactive_employee(employee_id):
    return desactive_employee(employee_id, request.json)

@employee_bp.route('/<int:employee_id>', methods=['DELETE'])
def delete_existing_employee(employee_id):
    return delete_employee(employee_id)

@employee_bp.route('/keycripyt/<string:pass>', methods=['GET'])
def get_key_cripyt():
    return send_encrypted_key()
