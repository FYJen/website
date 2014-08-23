import json
from flask import request

from app import ajen_webSite
from lib import status as custom_status
from resources.project import Project

@ajen_webSite.route('/api/project/<int:projectId>/', methods=['GET'])
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

@ajen_webSite.route('/api/project/', methods=['GET'])
def project_find():
    query_params = {
        'projectName': request.args.get('projectName', None),
        'deref': request.args.getlist('deref')
    }
    try:
        ProjectTasks = Project.find(**query_params)
        result = custom_status.HTTPOk(result=ProjectTasks)
    except custom_status.CustomStatus as e:
        result = e
    except Exception:
        result = custom_status.InternalServerError()

    return json.dumps(result.toDict())
