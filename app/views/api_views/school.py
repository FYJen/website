import json
from flask import request

from app import ajen_api
from lib import status as custom_status
from resources.school import School

@ajen_api.route('/api/school/<int:schoolId>/', methods=['GET'])
def school_get(schoolId):
    deref = request.args.getlist('deref')
    try:
        school = School.get(schoolId, deref=deref)
        result = custom_status.HTTPOk(result=school)
    except custom_status.CustomStatus as e:
        result = e
    except Exception:
        result = custom_status.InternalServerError()

    return json.dumps(result.toDict())

@ajen_api.route('/api/school/', methods=['GET'])
def school_find():
    query_params = {
        'name': request.args.get('name', None),
        'level': request.args.get('level', None),
        'attending': request.args.get('attending', None),
        'deref': request.args.getlist('deref')
    }
    try:
        schools = School.find(**query_params)
        result = custom_status.HTTPOk(result=schools)
    except custom_status.CustomStatus as e:
        result = e
    except Exception:
        result = custom_status.InternalServerError()

    return json.dumps(result.toDict())
