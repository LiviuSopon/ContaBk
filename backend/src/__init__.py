from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config_name):
    """
    Initialize the configuration for the Flask app.
    The config is taken from environment variables.
    If the required tables don't exist in the database, they will be created.
    Returns the app object used to instantiate the routes.
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
