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
        config = app_config['development']
    if not app_name:
        app_name = config.APP_NAME
    app = DefaultFlask(app_name)
    configure_app(app, config)
    configure_extensions(app)
    register_blueprints(app)
    configure_error_handlers(app)
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

def register_blueprints(app):
    """Register blueprints"""
    from app.apis.sample.route import sampleBP
    for bp in [sampleBP]:
        app.register_blueprint(bp)
    return app

def configure_error_handlers(app):
    """ Error handler subscribe """

    def handle_custom_api_exception(e):
        return e.to_result()

    def handle_unknown_exception(e):
        return DefaultResponse({}, str(e), HTTPStatus.INTERNAL_SERVER_ERROR)

    app.register_error_handler(Exception, handle_unknown_exception)
    app.register_error_handler(
        ValidationError, lambda err: DefaultResponse(
            {'error': str(err)}, 'Invalid request body', HTTPStatus.BAD_REQUEST
        )
    )
    app.register_error_handler(
        SchemaError, lambda err: DefaultResponse(
            {'error': str(err)}, 'Invalid schema at server',
            HTTPStatus.INTERNAL_SERVER_ERROR
        )
    )
    return app
