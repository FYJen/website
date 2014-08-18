import json
from flask import request

from app import ajen_webSite
from lib import status
from resources.work_place import Workplace

@ajen_webSite.route('/api/workplace/get/<int:workplace_id>/', methods=['GET'])
def workplace_get(workplace_id):
    deref = request.args.getlist('deref')
    try:
        result = Workplace.get(workplace_id, deref=deref)
    except status.ResourceNotFound as e:
        result = e.errors

    return json.dumps({'result': result})

@ajen_webSite.route('/api/workplace/find/', methods=['GET'])
def workplace_find():
    query_params = {
        'name': request.args.get('name', None),
        'initial': request.args.get('initial', None),
        'positionTitle': request.args.get('positionTitle', None),
        'deref': request.args.getlist('deref')
    }
    try:
        result = Workplace.find(**query_params)
    except status.ResourceNotFound as e:
        result = e.errors

    return json.dumps({'result': result})