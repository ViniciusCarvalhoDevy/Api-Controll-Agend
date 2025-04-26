from models.models import Agend
from models.models import db
from models.models import AgendHasServingSalon, Employee, Hours,ServingSalon
from flask import jsonify, request
from datetime import datetime
from services.code.handleErros import safe_commit

def get_all_agends():
    agends = Agend.query.all()
    return jsonify([{'idAgend': a.idAgend, 'Employee_idEmployee': a.Employee_idEmployee, 'Hours_idHours': a.Hours_idHours,
                     'client': a.client, 'value': a.value, 'obs': a.obs, 'date': str(a.date)} for a in agends])
    
# format parametro ?dateAgend=2025-04-17&idEmployee=1
def get_free_agends_for_date():
    dateAgend = request.args.get('dateAgend')  # Obtendo o parâmetro via query string
    idEmployee = request.args.get('idEmployee')
    dateAgend = datetime.strptime(dateAgend,"%Y-%m-%d")
    dateAgend = dateAgend.date()
    if not dateAgend or not idEmployee:
        return jsonify({'error': 'Parâmetros insuficientes'}), 400
    hours_agend = Hours.query.outerjoin(Agend, (Hours.idHours == Agend.Hours_idHours and Agend.date == dateAgend)).filter_by(Employee_idEmployee=idEmployee,date=dateAgend).all()
    hours = Hours.query.all()
    hours_free = []
    for h in hours:
        if  h.hours not in [i.hours for i in hours_agend]:
            hours_free.append(h)
    return jsonify([{'idHoursFree': hf.idHours, 'hoursFree': str(hf.hours)} for hf in hours_free])
    
def get_all_agends_with_serving():
    agends = Agend.query.all()
    agend_has_serving_salon = AgendHasServingSalon.query.all()
    return jsonify([{'idAgend': a.idAgend, 'Employee_Name': Employee.query.get(a.Employee_idEmployee).name, 'Hours_idHours': str(Hours.query.get(a.Hours_idHours).hours),
                     'client': a.client, 'value': a.value, 'obs': a.obs, 'date': str(a.date),
                     'Servin_Salon_idserving_salon':[ServingSalon.query.get(s.Servin_Salon_idserving_salon).description for s in agend_has_serving_salon if s.Agend_idAgend == a.idAgend],} for a in agends])

def get_agend_with_serving_for_id(agend_id):
    agend = Agend.query.get(agend_id)
    agend_has_serving_salon = AgendHasServingSalon.query.all()
    return jsonify({'idAgend': agend.idAgend, 'Employee_Name': Employee.query.get(agend.Employee_idEmployee).name, 'Hours_idHours': str(Hours.query.get(agend.Hours_idHours).hours),
                     'client': agend.client, 'value': agend.value, 'obs': agend.obs, 'date': str(agend.date),
                     'Servin_Salon_idserving_salon':[ServingSalon.query.get(s.Servin_Salon_idserving_salon).description for s in agend_has_serving_salon if s.Agend_idAgend == agend.idAgend]})
    
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
    safe_commit(db.session)   
    return jsonify({'message': 'Agend created','Agend': {'idAgend': new_agend.idAgend, 'Employee_idEmployee': new_agend.Employee_idEmployee, 'Hours_idHours': new_agend.Hours_idHours,
                     'client': new_agend.client, 'value': new_agend.value, 'obs': new_agend.obs, 'date': str(new_agend.date)}}), 201

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
    safe_commit(db.session) 
    return jsonify({'message': 'Agend updated','Agend': {'idAgend': agend.idAgend, 'Employee_idEmployee': agend.Employee_idEmployee, 'Hours_idHours': agend.Hours_idHours,
                     'client': agend.client, 'value': agend.value, 'obs': agend.obs, 'date': str(agend.date)}}), 200

def delete_agend(agend_id):
    agend = Agend.query.get(agend_id)
    if not agend:
        return jsonify({'message': 'Agend not found'}), 404
    db.session.delete(agend)
    safe_commit(db.session)
    return jsonify({'message': 'Agend deleted'}), 200
