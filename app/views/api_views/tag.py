import json
from flask import request

from app import ajen_api
from lib import status as custom_status
from resources.tag import Tag

@ajen_api.route('/api/tag/<int:tagId>/', methods=['GET'])
def tag_get(tagId):
    deref = request.args.getlist('deref')
    try:
        user = Tag.get(tagId, deref=deref)
        result = custom_status.HTTPOk(result=user)
    except custom_status.CustomStatus as e:
        result = e
    except Exception:
        result = custom_status.InternalServerError()

    return json.dumps(result.toDict())

@ajen_api.route('/api/tag/', methods=['GET'])
def tag_find():
    query_params = {
        'name': request.args.get('name', None),
        'deref': request.args.getlist('deref')
    }
    try:
        tags = Tag.find(**query_params)
        result = custom_status.HTTPOk(result=tags)
    except custom_status.CustomStatus as e:
        result = e
    except Exception:
        result = custom_status.InternalServerError()

    return json.dumps(result.toDict())
