import json
from flask import request

from app import ajen_api
from lib import status as custom_status
from resources.address import Address

@ajen_api.route('/api/address/<int:addressId>/', methods=['GET'])
def address_get(addressId):
    deref = request.args.getlist('deref')
    stringnify = True if request.args.get('stringnify', '').lower() == 'true' \
                 else False
    try:
        address = Address.get(addressId, stringnify=stringnify, deref=deref)
        result = custom_status.HTTPOk(result=address)
    except custom_status.CustomStatus as e:
        result = e
    except Exception:
        result = custom_status.InternalServerError()

    return json.dumps(result.toDict())

@ajen_api.route('/api/address/', methods=['GET'])
def address_find():
    query_params = {
        'active': request.args.get('active', None),
        'country': request.args.get('country', None),
        'postalCode': request.args.get('postalCode', None),
        'zipCode': request.args.get('zipCode', None),
        'stringnify': True if request.args.get('stringnify', '').lower() == \
                      'true' else False,
        'deref': request.args.getlist('deref')
    }

    try:
        addresses = Address.find(**query_params)
        result = custom_status.HTTPOk(result=addresses)
    except custom_status.CustomStatus as e:
        result = e
    except Exception:
        result = custom_status.InternalServerError()

    return json.dumps(result.toDict())
