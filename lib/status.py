"""Custom Status.
"""
class CustomStatus(Exception):
    """
    """
    def __init__(self, msg=None, details={}, result={}):
        self.statusCode = self.__class__.__name__
        self.statusMsg = msg
        self.statusDetails = details
        self.result = result

    def toDict(self):
        return {
            'result': self.result,
            'status': {
                'statusCode': self.statusCode,
                'statusMsg': self.statusMsg,
                'statusDetails': self.statusDetails
            }
        }

class HTTPOk(CustomStatus):
    def __init__(self, msg='OK', **kwargs):
        CustomStatus.__init__(self, msg=msg, **kwargs)

class ResourceNotFound(CustomStatus):
    def __init__(self, msg='Resource not found', **kwargs):
        CustomStatus.__init__(self, msg=msg, **kwargs)

class InvalidRequest(CustomStatus):
    def __init__(self, msg='Inavlid request', **kwargs):
        CustomStatus.__init__(self, msg=msg, **kwargs)
