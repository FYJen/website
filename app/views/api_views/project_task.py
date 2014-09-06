import json
from flask import request

from app import ajen_api
from lib import status as custom_status
from resources.project_task import ProjectTask

@ajen_api.route('/api/projecttask/<int:projectTaskId>/', methods=['GET'])
def projectTask_get(projectTaskId):
    deref = request.args.getlist('deref')
    try:
        projectTask = ProjectTask.get(projectTaskId, deref=deref)
        result = custom_status.HTTPOk(result=projectTask)
    except custom_status.CustomStatus as e:
        result = e
    except Exception:
        result = custom_status.InternalServerError()

    return json.dumps(result.toDict())

@ajen_api.route('/api/projecttask/', methods=['GET'])
def projectTask_find():
    query_params = {
        'projectName': request.args.get('projectName', None),
        'deref': request.args.getlist('deref')
    }
    try:
        ProjectTasks = ProjectTask.find(**query_params)
        result = custom_status.HTTPOk(result=ProjectTasks)
    except custom_status.CustomStatus as e:
        result = e
    except Exception:
        result = custom_status.InternalServerError()

    return json.dumps(result.toDict())
