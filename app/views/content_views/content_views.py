from collections import OrderedDict
from flask import render_template, abort
import json
import requests

from app import ajen_webSite, ajen_api
from app.config import default_config as setting

HOST = ajen_api.config['SERVER_NAME']
QUERY = 'http://%s/api/%s/%s'

@ajen_webSite.route('/', methods=['GET'])
@ajen_webSite.route('/about/', methods=['GET'])
def about():
    return render_template('about.html', headers=setting.BASE_PAGE)

@ajen_webSite.route('/resume/<string:displayType>/')
@ajen_webSite.route('/resume/', methods=['GET'])
def resume(displayType='html'):
    try:
        params = {
            'deref': ['address', 'skills', 'workPlaces', 'projects', 'schools']
        }
        resume = requests.get(QUERY % (HOST, 'user', 1), params=params)
    except Exception:
        abort(500)

    # Even requests library comes with json function, we will use the string
    # content to convert to json specifically because the order is important to us.
    # Hooking up json.loads() with OrderedDict to achieve that functionality.
    resume = json.loads(resume.content, object_pairs_hook=OrderedDict)

    if resume['status']['statusCode'] == 'HTTPOk' and resume['result']:
        displayType = displayType.lower()

        # Check which formate we should use: either JSON or HTML. If it is JSON
        # we will dump the JSON using json.dumps, else we will just return the
        # resume variable.
        if displayType == 'json':
            resume = json.dumps(resume['result'])
        elif displayType == 'html':
            resume = resume['result']
        else:
            abort(404)

        return render_template('resume.html', headers=setting.BASE_PAGE,
                                resume=resume, displayType=displayType)

    elif resume['status']['statusCode'] == 'InternalServerError':
        abort(500)
    else:
        abort(404)

@ajen_webSite.route('/projects/', methods=['GET'])
def projects():
    try:
        projects = requests.get(QUERY % (HOST, 'project', ''),
                                params={'deref': 'tasks'})
    except Exception:
        abort(500)

    projects = projects.json()
    if projects['status']['statusCode'] == 'HTTPOk' and projects['result']:
        return render_template('projects.html', headers=setting.BASE_PAGE,
                               projects=projects['result'])
    elif projects['status']['statusCode'] == 'InternalServerError':
        abort(500)
    else:
        abort(404)

@ajen_webSite.route('/contact/', methods=['GET'])
def contact():
    try:
        user = requests.get(QUERY % (HOST, 'user', 1))
    except Exception:
        abort(500)

    user = user.json()
    if user['status']['statusCode'] == 'HTTPOk' and user['result']:
        return render_template('contact.html', headers=setting.BASE_PAGE,
                               user=user['result'])
