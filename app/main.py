from http import HTTPStatus
from jsonschema import ValidationError
from jsonschema import SchemaError
from app.settings.configs import app_config
from app.settings.custom_flask import DefaultFlask
from app.settings.custom_flask import MongoJSONEncoder
from app.settings.custom_flask import ObjectIdConverter
from app.settings.custom_response import DefaultResponse

__all__ = ['create_app']

def create_app(config=None, app_name=None):
    """Create an app instance based on the passed params"""
    if not config:
        config = app_config.get('development')
    if not app_name:
        app_name = Config.APP_NAME
    app = DefaultFlask(app_name)
    app = configure_app(app, config)
    return app

def configure_app(app, config=None):
    app.config.from_object(config)
    return app

def configure_extensions(app):
    """Configure Extensions"""
    from app.settings.extensions import db
    db.init_app(app)
    app.json_encoder = MongoJSONEncoder
    app.url_map.converters['objectid'] = ObjectIdConverter
