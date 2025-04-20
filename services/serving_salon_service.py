from models.models import ServingSalon,db
from flask import jsonify

def get_all_servings():
    serving = ServingSalon.query.all()
    return jsonify([{'idserving_salon': s.idserving_salon, 'description': s.description} for s in serving])

def get_serving_by_id(serving_id):
    serving = ServingSalon.query.get(serving_id)
    if not serving:
        return jsonify({'message': 'serving not found'}), 404
    return jsonify({'idserving_salon': serving.idserving_salon, 'description': serving.description})

def create_serving(data):
    new_serving = ServingSalon(description=data['description'])
    db.session.add(new_serving)
    db.session.commit()
    return jsonify({'message': 'serving created'}), 201

def update_serving(serving_id, data):
    serving = ServingSalon.query.get(serving_id)
    if not serving:
        return jsonify({'message': 'serving not found'}), 404
    serving.description = data['description']
    db.session.commit()
    return jsonify({'message': 'serving updated'}), 200

def delete_serving(serving_id):
    serving = ServingSalon.query.get(serving_id)
    if not serving:
        return jsonify({'message': 'serving not found'}), 404
    db.session.delete(serving)
    db.session.commit()
    return jsonify({'message': 'serving deleted'}), 200
