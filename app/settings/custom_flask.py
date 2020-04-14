from flask import Flask
from datetime import datetime, date
import isodate as iso
from bson import ObjectId
from flask.json import JSONEncoder
from werkzeug.routing import BaseConverter
from app.settings.custom_response import DefaultResponse


class DefaultFlask(Flask):
    """Override the Flask class to handle custom JSON Api Responses"""
    def make_response(self, rv):
        """Override Flask().make_response()
        Check if the type is ApiResult, then return ApiResult().to_response().
        """
        if isinstance(rv, DefaultResponse):
            return rv.to_response()
        return Flask.make_response(self, rv)

class MongoJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime, date)):
            return iso.datetime_isoformat(o)
        if isinstance(o, ObjectId):
            return str(o)
        else:
            return super().default(o)


class ObjectIdConverter(BaseConverter):
    def to_python(self, value):
        return ObjectId(value)

    def to_url(self, value):
        return str(value)
