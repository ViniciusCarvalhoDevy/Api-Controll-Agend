from models.models import AgendHasServingSalon
from models.models import db
from flask import jsonify

def create_agend_service_salon(data):
    new_link = AgendHasServingSalon(ServingSalon_idServingSalon=data['ServingSalon_idServingSalon'],
                                 Agend_idAgend=data['Agend_idAgend'])
    db.session.add(new_link)
    db.session.commit()
    return jsonify({'message': 'Agend-ServingSalon link created'}), 201
