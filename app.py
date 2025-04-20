from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from routes.employee_routes import employee_bp
from routes.hours_routes import hours_bp
from routes.serving_salon_routes import serving_salon_bp
from routes.agend_routes import agend_bp
from models.models import db


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(employee_bp, url_prefix='/employee')
app.register_blueprint(hours_bp, url_prefix='/hours')
app.register_blueprint(serving_salon_bp, url_prefix='/serving-salon')
app.register_blueprint(agend_bp, url_prefix='/agend')

app.run(debug=True)
