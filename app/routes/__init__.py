"""
routes/__init__.py

This module initializes the routes blueprint.
"""
from flask import Blueprint
# Import route modules to register them with the blueprint
from .image_generation_routes_blueprint import image_generation_routes
from .chatgpt_routes_blueprint import chatgpt_routes

# Create a Blueprint object for your routes
routes_blueprint = Blueprint('routes', __name__)

# Register route modules associated with the Image Generation blueprint
routes_blueprint.register_blueprint(image_generation_routes)

# Register route modules associated with the ChatGPT blueprint
routes_blueprint.register_blueprint(chatgpt_routes)
