from models.models import Agend
from models.models import db
from models.models import AgendHasServingSalon, Employee, Hours,ServingSalon
from flask import jsonify

def get_all_agends():
    agends = Agend.query.all()
    return jsonify([{'idAgend': a.idAgend, 'Employee_idEmployee': a.Employee_idEmployee, 'Hours_idHours': a.Hours_idHours,
                     'client': a.client, 'value': a.value, 'obs': a.obs, 'date': str(a.date)} for a in agends])
    
def get_all_agends_with_serving():
    agends = Agend.query.all()
    agend_has_serving_salon = AgendHasServingSalon.query.all()
    print([s.Servin_Salon_idserving_salon for s in agend_has_serving_salon if s.Agend_idAgend == 1])
    return jsonify([{'idAgend': a.idAgend, 'Employee_Name': Employee.query.get(a.Employee_idEmployee).name, 'Hours_idHours': Hours.query.get(a.Hours_idHours).hours,
                     'client': a.client, 'value': a.value, 'obs': a.obs, 'date': str(a.date),
                     'Servin_Salon_idserving_salon':[ServingSalon.query.get(s.Servin_Salon_idserving_salon).description for s in agend_has_serving_salon if s.Agend_idAgend == a.idAgend],} for a in agends])
    
def get_agend_by_id(agend_id):
    agend = Agend.query.get(agend_id)
    if not agend:
        return jsonify({'message': 'Agend not found'}), 404
    return jsonify({'idAgend': agend.idAgend, 'Employee_idEmployee': agend.Employee_idEmployee,
                    'Hours_idHours': agend.Hours_idHours, 'client': agend.client, 'value': agend.value,
                    'obs': agend.obs, 'date': str(agend.date)})

def create_agend(data):
    new_agend = Agend(Employee_idEmployee=data['Employee_idEmployee'], Hours_idHours=data['Hours_idHours'],
                      client=data['client'], value=data['value'], obs=data['obs'], date=data['date'])
    db.session.add(new_agend)
    db.session.commit()
    return jsonify({'message': 'Agend created'}), 201

def update_agend(agend_id, data):
    agend = Agend.query.get(agend_id)
    if not agend:
        return jsonify({'message': 'Agend not found'}), 404
    agend.Employee_idEmployee = data['Employee_idEmployee']
    agend.Hours_idHours = data['Hours_idHours']
    agend.client = data['client']
    agend.value = data['value']
    agend.obs = data['obs']
    agend.date = data['date']
    db.session.commit()
    return jsonify({'message': 'Agend updated'}), 200

def delete_agend(agend_id):
    agend = Agend.query.get(agend_id)
    if not agend:
        return jsonify({'message': 'Agend not found'}), 404
    db.session.delete(agend)
    db.session.commit()
    return jsonify({'message': 'Agend deleted'}), 200
