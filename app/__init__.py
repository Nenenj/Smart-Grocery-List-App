#!/usr/bin/env python3

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from dotenv import load_dotenv
from instance.config import Config


load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config['SECRET_KEY'] = os.getenv(
            'SECRET_KEY', 'default_secret_key'
            )
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
            'DADBASE_URL', 'sqlite:///default.db'
            )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Debug print statements to check configurations
    print('Config file loaded successfully.')
    print(f"SECRET_KEY: {app.config.get('SECRET_KEY')}")
    print(
            f"SQLALCHEMY_DATABASE_URl: " 
            "{app.config.get('SQLALCHEMY_DATABASE_URl')}"
            )

    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return user.query.get(init(user_id))

    from app.routes import init_routes
    init_routes(app)

    return app
