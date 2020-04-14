from abc import ABC, abstractmethod
from flask import Response
import json


class ResponseInterface(ABC):
    @abstractmethod
    def _format_response(self):
        """Format the response before issuing it out"""
        pass

    @abstractmethod
    def to_response(self):
        """Return a Flask Response object"""
        pass


class DefaultResponse(ResponseInterface):
    """default response - JSON response"""

    def __init__(
            self, data, message=None, status=200, error_code=None
    ):
        if type(data) != dict and type(data) != list:
            raise Exception

        self.data = data
        self.message = message
        self.status = status
        self.error_code = error_code

    def _format_response(self):
        pass

    def to_response(self):
        """Return a JSON response"""
        self._format_response()
        response = {
            'message': self.message,
            'error_code': self.error_code,
            'payload': self.data
        }

        result = Response(
            json.dumps(response), self.status, mimetype='application/json'
        )
        return result
