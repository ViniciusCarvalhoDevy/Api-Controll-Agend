from models.models import Employee
from models.models import db
from flask import jsonify

def get_all_employees():
    employees = Employee.query.all()
    return jsonify([{'idEmployee': e.idEmployee, 'name': e.name, 'phone': e.phone, 'email': e.email} for e in employees])

def get_employee_by_id(employee_id):
    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404
    return jsonify({'idEmployee': employee.idEmployee, 'name': employee.name, 'phone': employee.phone, 'email': employee.email})

def create_employee(data):
    new_employee = Employee(name=data['name'], phone=data['phone'], email=data['email'])
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
    db.session.commit()
    return jsonify({'message': 'Employee updated'}), 200

def delete_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404
    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message': 'Employee deleted'}), 200
