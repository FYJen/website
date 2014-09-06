import json
from flask import request

from app import ajen_api
from lib import status as custom_status
from resources.project import Project

@ajen_api.route('/api/project/<int:projectId>/', methods=['GET'])
def project_get(projectId):
    deref = request.args.getlist('deref')
    try:
        project = Project.get(projectId, deref=deref)
        result = custom_status.HTTPOk(result=project)
    except custom_status.CustomStatus as e:
        result = e
    except Exception:
        result = custom_status.InternalServerError()

    return json.dumps(result.toDict())

@ajen_api.route('/api/project/', methods=['GET'])
def project_find():
    query_params = {
        'projectName': request.args.get('projectName', None),
        'deref': request.args.getlist('deref')
    }
    try:
        projects = Project.find(**query_params)
        print 'In project'
        result = custom_status.HTTPOk(result=projects)
    except custom_status.CustomStatus as e:
        result = e
    except Exception:
        result = custom_status.InternalServerError()

    return json.dumps(result.toDict())
