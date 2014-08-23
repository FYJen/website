import json
from flask import request

from app import ajen_webSite
from lib import status as custom_status
from resources.skill import Skill

@ajen_webSite.route('/api/skill/<int:skillId>/', methods=['GET'])
def skill_get(skillId):
    deref = request.args.getlist('deref')
    try:
        skill = Skill.get(skillId, deref=deref)
        result = custom_status.HTTPOk(result=skill)
    except custom_status.CustomStatus as e:
        result = e
    except Exception:
        result = custom_status.InternalServerError()

    return json.dumps(result.toDict())

@ajen_webSite.route('/api/skill/', methods=['GET'])
def skill_find():
    query_params = {
        'description': request.args.get('description', None),
        'tag': request.args.get('tag', None),
        'userId': request.args.get('userId', None),
        'deref': request.args.getlist('deref')
    }
    try:
        skills = Skill.find(**query_params)
        result = custom_status.HTTPOk(result=skills)
    except custom_status.CustomStatus as e:
        result = e
    except Exception:
        result = custom_status.InternalServerError()

    return json.dumps(result.toDict())