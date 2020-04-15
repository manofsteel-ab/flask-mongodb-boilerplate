from flask import Blueprint
from flask import request
from http import HTTPStatus

from app.settings.custom_response import DefaultResponse
from app.apis.sample.managers.sample import SampleManager

sampleBP = Blueprint('sample', __name__, url_prefix='/api/sample')


@sampleBP.route('/health/', methods=['GET'])
def sample():
    return DefaultResponse(
        {}, 'Success', status=HTTPStatus.OK
    )

@sampleBP.route('/dump/', methods=['POST'])
def sample_dump():
    data = request.json
    SampleManager().create_entry(sample_data_attributes=data)
    return DefaultResponse(
        {}, 'Success', status=HTTPStatus.CREATED
    )

@sampleBP.route('/list/', methods=['GET'])
def sample_list():
    obj_list = SampleManager().get_list()
    print(obj_list)
    return DefaultResponse(
        data={
            'list':[val.to_dict() for val in obj_list]
        },
        message='Success', status=HTTPStatus.CREATED
    )
