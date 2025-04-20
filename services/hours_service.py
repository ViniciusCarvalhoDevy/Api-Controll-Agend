from models.models import Hours
from models.models import db
from flask import jsonify

def get_all_hours():
    hours = Hours.query.all()
    return jsonify([{'idHours': h.idHours, 'hours': str(h.hours)} for h in hours])

def get_hour_by_id(hour_id):
    hour = Hours.query.get(hour_id)
    if not hour:
        return jsonify({'message': 'Hour not found'}), 404
    return jsonify({'idHours': hour.idHours, 'hours': str(hour.hours)})

def create_hour(data):
    new_hour = Hours(hours=data['hours'])
    db.session.add(new_hour)
    db.session.commit()
    return jsonify({'message': 'Hour created'}), 201

def update_hour(hour_id, data):
    hour = Hours.query.get(hour_id)
    if not hour:
        return jsonify({'message': 'Hour not found'}), 404
    hour.hours = data['hours']
    db.session.commit()
    return jsonify({'message': 'Hour updated'}), 200

def delete_hour(hour_id):
    hour = Hours.query.get(hour_id)
    if not hour:
        return jsonify({'message': 'Hour not found'}), 404
    db.session.delete(hour)
    db.session.commit()
    return jsonify({'message': 'Hour deleted'}), 200
