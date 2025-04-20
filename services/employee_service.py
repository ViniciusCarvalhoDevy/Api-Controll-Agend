from models.models import Employee
from models.models import db
from flask import jsonify
from .code.functions import cript_password
import os

def get_all_employees():
    employees = Employee.query.all()
    return jsonify([{'idEmployee': e.idEmployee, 'name': e.name, 'phone': e.phone, 'email': e.email,activate=data['activate']} for e in employees])

def get_employee_by_id(employee_id):
    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404
    return jsonify({'idEmployee': employee.idEmployee, 'name': employee.name, 'phone': employee.phone, 'email': employee.email})

def get_employee_password_by_id(employee_id):
    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404
    return jsonify({'idEmployee': employee.idEmployee, 'name': employee.name, 'phone': employee.phone, 'email': employee.email,'password':employee.password,activate=data['activate']})

def create_employee(data):
    password_crypt= cript_password(data=['password'])
    new_employee = Employee(name=data['name'], phone=data['phone'], email=data['email'], password=password_crypt, activate=data['activate'])
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'message': 'Employee created'}), 201

def update_employee(employee_id, data):
    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404
    employee.name = data['name']
    employee.phone = data['phone']
    employee.email = data['email']
    employee.activate = data['activate']
    password_crypt = cript_password(data['password'])
    employee.password = password_crypt
    db.session.commit()
    return jsonify({'message': 'Employee updated'}), 200

def delete_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404
    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message': 'Employee deleted'}), 200

def send_encrypted_key(passw):
    if passw = os.getenv("PASSWORD_FOR_KEY"):
        chave_secreta = os.getenv("FERNET_SECRET_KEY")
        if not chave_secreta:
            return jsonify({'error': 'Chave não encontrada'}), 404
        return jsonify({'key': chave_secreta})
    else 
        return  jsonify({'error': 'Senha invalida'}), 404
