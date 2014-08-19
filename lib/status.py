"""Custom Exceptions.
"""

class ResourceNotFound(Exception):
    def __init__(self, resourceType, **kwargs):
        errMessage = {
            'statusMessage': 'Resource Not Found',
            'resourceType': resourceType
        }
        for k, v in kwargs.iteritems():
            errMessage[k] = v
        self.errors = errMessage

class InvalidRequest(Exception):
    def __init__(self, resourceType, **kwargs):
        errMessage = {
            'statusMessage': 'Invalid Request',
            'resourceType': resourceType
        }
        for k, v in kwargs.iteritems():
            errMessage[k] = v
        self.errors = errMessage

