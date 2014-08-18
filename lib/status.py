"""Custom Exceptions.
"""

class ResourceNotFound(Exception):
    def __init__(self, resourceType, **kwargs):
        errMessage = {
            'message': '404: Resource Not Found',
            'resourceType': resourceType
        }
        for k, v in kwargs.iteritems():
            errMessage[k] = v
        self.errors = errMessage

