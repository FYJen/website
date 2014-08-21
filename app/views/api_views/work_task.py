import json
from flask import request

from app import ajen_webSite
from lib import status as custom_status
from resources.work_task import Worktask

@ajen_webSite.route('/api/worktask/<int:worktaskId>/', methods=['GET'])
def worktask_get(worktaskId):
    deref = request.args.getlist('deref')
    try:
        workTask = Worktask.get(worktaskId, deref=deref)
        result = custom_status.HTTPOk(result=workTask)
    except Exception as e:
        result = e

    return json.dumps(result.toDict())

@ajen_webSite.route('/api/worktask/', methods=['GET'])
def worktask_find():
    query_params = {
        'workPlaceName': request.args.get('workPlaceName', None),
        'initial': request.args.get('initial', None),
        'deref': request.args.getlist('deref')
    }
    try:
        workTasks = Worktask.find(**query_params)
        result = custom_status.HTTPOk(result=workTasks)
    except Exception as e:
        result = e

    return json.dumps(result.toDict())
