import json
from flask import request

from app import ajen_api
from lib import status as custom_status
from resources.work_place import Workplace

@ajen_api.route('/api/workplace/<int:workplaceId>/', methods=['GET'])
def workplace_get(workplaceId):
    deref = request.args.getlist('deref')
    try:
        workPlace = Workplace.get(workplaceId, deref=deref)
        result = custom_status.HTTPOk(result=workPlace)
    except custom_status.CustomStatus as e:
        result = e
    except Exception:
        result = custom_status.InternalServerError()

    return json.dumps(result.toDict())

@ajen_api.route('/api/workplace/', methods=['GET'])
def workplace_find():
    query_params = {
        'name': request.args.get('name', None),
        'initial': request.args.get('initial', None),
        'positionTitle': request.args.get('positionTitle', None),
        'deref': request.args.getlist('deref')
    }
    try:
        workPlaces = Workplace.find(**query_params)
        result = custom_status.HTTPOk(result=workPlaces)
    except custom_status.CustomStatus as e:
        result = e
    except Exception:
        result = custom_status.InternalServerError()

    return json.dumps(result.toDict())
