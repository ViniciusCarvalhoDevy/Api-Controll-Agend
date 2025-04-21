from models.models import AgendHasServingSalon
from models.models import db
from flask import jsonify
from services.code.handleErros import safe_commit

def create_agend_service_salon(data):

    servings = data['Servin_Salon_idserving_salon']
    new_link = []
    for s in servings:
        exist_serving_in_agend = AgendHasServingSalon.query.filter_by(Servin_Salon_idserving_salon=s,Agend_idAgend=data['Agend_idAgend']).all()
        if exist_serving_in_agend:
            return jsonify({'message': f'Agend-ServingSalon with id={s} alreary exist in agend'}), 404
        new_link.append(AgendHasServingSalon(Servin_Salon_idserving_salon=s, Agend_idAgend=data['Agend_idAgend']))

    db.session.add_all(new_link)
    safe_commit(db.session)
    return jsonify({'message': f'Agend-ServingSalon add'}), 404
