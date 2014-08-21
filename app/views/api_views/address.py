import json
from flask import request

from app import ajen_webSite
from lib import status as custom_status
from resources.address import Address

@ajen_webSite.route('/api/address/<int:address_id>/', methods=['GET'])
def address_get(address_id):
    deref = request.args.getlist('deref')
    stringlized = True if request.args.get('stringlize', '').lower() == 'true' \
                 else False
    try:
        address = Address.get(address_id, stringlized=stringlized, deref=deref)
        result = custom_status.HTTPOk(result=address)
    except Exception as e:
        result = e

    return json.dumps(result.toDict())

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
        addresses = Address.find(**query_params)
        result = custom_status.HTTPOk(result=addresses)
    except Exception as e:
        result = e

    return json.dumps(result.toDict())
