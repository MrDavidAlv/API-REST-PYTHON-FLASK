from flask import Flask
from flask_jwt_extended import JWTManager
from models import db
from config import Config
from routes import register_blueprints

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
jwt = JWTManager(app)

register_blueprints(app)

if __name__ == '__main__':
    app.run(debug=True)
