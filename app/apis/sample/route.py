from flask import Blueprint, request
from http import HTTPStatus

from app.settings.custom_response import DefaultResponse

sampleBP = Blueprint('sample', __name__, url_prefix='/api/sample')


@sampleBP.route('/', methods=['POST', 'GET'])
def sample():
    return DefaultResponse(
        {}, 'Success', status=HTTPStatus.CREATED
    )
