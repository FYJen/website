import json
from flask import request

from app import ajen_webSite
from lib import status as custom_status
from resources.user import User

@ajen_webSite.route('/api/user/<int:userId>/', methods=['GET'])
def user_get(userId):
    deref = request.args.getlist('deref')
    try:
        user = User.get(userId, deref=deref)
        result = custom_status.HTTPOk(result=user)
    except custom_status.CustomStatus as e:
        result = e
    except Exception:
        result = custom_status.InternalServerError()

    return json.dumps(result.toDict())

@ajen_webSite.route('/api/user/', methods=['GET'])
def user_find():
    query_params = {
        'email': request.args.get('email', None),
        'firstName': request.args.get('firstName', None),
        'lastName': request.args.get('lastName', None),
        'phone': request.args.get('phone', None),
        'deref': request.args.getlist('deref')
    }
    try:
        users = User.find(**query_params)
        result = custom_status.HTTPOk(result=users)
    except custom_status.CustomStatus as e:
        result = e
    except Exception:
        result = custom_status.InternalServerError()

    return json.dumps(result.toDict())
