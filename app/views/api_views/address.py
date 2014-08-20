import json
from flask import request

from app import ajen_webSite
from resources.address import Address

@ajen_webSite.route('/api/address/<int:address_id>/', methods=['GET'])
def address_get(address_id):
    deref = request.args.getlist('deref')
    stringlized = True if request.args.get('stringlize', '').lower() == 'true' \
                 else False
    try:
        result = Address.get(address_id, stringlized=stringlized, deref=deref)
    except Exception as e:
        result = e.errors

    return json.dumps({'result': result})

@ajen_webSite.route('/api/address/', methods=['GET'])
def address_find():
    query_params = {
        'active': request.args.get('active', None),
        'country': request.args.get('country', None),
        'postalCode': request.args.get('postalCode', None),
        'zipCode': request.args.get('zipCode', None),
        'stringlized': True if request.args.get('stringlize', '').lower() == \
                      'true' else False,
        'deref': request.args.getlist('deref')
    }

    try:
        result = Address.find(**query_params)
    except Exception as e:
        result = e.errors

    return json.dumps({'result': result})
