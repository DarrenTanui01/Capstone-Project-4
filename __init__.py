from flask import Flask
from database import db
from routes.auth import auth_bp
from routes.group import group_bp
from routes.transaction import transaction_bp
from routes.savings import savings_bp
from routes.communication import communication_bp
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///proxima.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Change this!

    db.init_app(app)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(group_bp, url_prefix='/api')
    app.register_blueprint(transaction_bp, url_prefix='/api')
    app.register_blueprint(savings_bp, url_prefix='/api')
    app.register_blueprint(communication_bp, url_prefix='/api')

    jwt = JWTManager(app)

    with app.app_context():
        db.create_all()

    return app