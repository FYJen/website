import json
from flask import request

from app import ajen_webSite
from lib import status as custom_status
from resources.work_place import Workplace

@ajen_webSite.route('/api/workplace/<int:workplace_id>/', methods=['GET'])
def workplace_get(workplace_id):
    deref = request.args.getlist('deref')
    try:
        workPlace = Workplace.get(workplace_id, deref=deref)
        result = custom_status.HTTPOk(result=workPlace)
    except Exception as e:
        result = e

    return json.dumps(result.toDict())

@ajen_webSite.route('/api/workplace/', methods=['GET'])
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
    except Exception as e:
        result = e

    return json.dumps(result.toDict())
