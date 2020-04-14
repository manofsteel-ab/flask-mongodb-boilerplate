from flask import Flask

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
