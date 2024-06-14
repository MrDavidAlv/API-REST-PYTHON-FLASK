from flask import Blueprint

from routes.auth import auth_bp
from routes.tasks import tasks_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
