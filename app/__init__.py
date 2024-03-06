# app/__init__.py

from flask import Flask
from flask_cors import CORS


def create_app():
    """
    Create and configure the Flask application instance.
    """
    app = Flask(__name__)

    # Enable CORS for all routes in the application
    CORS(app)

    # Import and register blueprints
    from .routes import routes_blueprint
    app.register_blueprint(routes_blueprint)

    # Other configuration and setup code goes here...

    return app
