import json
from flask import request

from app import ajen_webSite
from lib import status as custom_status
from resources.work_task import Worktask

@ajen_webSite.route('/api/worktask/<int:worktask_id>/', methods=['GET'])
def worktask_get(worktask_id):
    deref = request.args.getlist('deref')
    try:
        result = Worktask.get(worktask_id, deref=deref)
    except custom_status.ResourceNotFound as e:
        result = e.errors

    return json.dumps({'result': result})

@ajen_webSite.route('/api/worktask/', methods=['GET'])
def worktask_find():
    query_params = {
        'workPlaceName': request.args.get('workPlaceName', None),
        'initial': request.args.get('initial', None),
        'deref': request.args.getlist('deref')
    }
    try:
        result = Worktask.find(**query_params)
    except custom_status.ResourceNotFound as e:
        result = e.errors

    return json.dumps({'result': result})