from dbmodels import models
from collections import OrderedDict
from flask import jsonify

from lib import status

DEREF_LIST = ['workplace']

class Worktask(object):
    """Worktask resources.
    """
    @classmethod
    def get(cls, workTaskId, deref=[]):
        """Get workTask by workTaskId.

        Args:
            workTaskId - A specified workTask Id.
            deref - A list of fields to deref.

        Returns:
            A serialized WorkTask JSON dict.
        """
        cls.__validateDeref(deref)
        workTask = models.WorkTask.query.get(workTaskId)

        if not workTask:
            raise status.ResourceNotFound('WorkTask', resourceId=workTaskId)

        return cls.__to_Dict([workTask], deref)[0]

    @classmethod
    def find(cls, workPlaceName=None, deref=[]):
        """Find workTasks that meet the expected query parameters.

        Args:
            workPlaceName - The name of the company.

        Returns:
            A list of matched and serialized WorkTask objects.
        """
        pass

    @classmethod
    def update(cls, workTaskId, **kwargs):
        """Update specified workPlace with given arguments. 
        """
        raise NotImplementedError('WorkTask Resource - update method is currently '
                                  'not supported.')

    @classmethod
    def create(cls, description=None, workplace_id=None):
        """Create a new workPlace entry.
        """
        raise NotImplementedError('WorkTask Resource - create method is currently '
                                  'not supported.')

    @classmethod
    def __validateDeref(cls, derefList):
        """Validate the deref list in the query string.
        """
        for deref in derefList:
            if deref not in DEREF_LIST:
                derefList.remove(deref)

    @classmethod
    def __to_Dict(cls, workTaskObjects, deref):
        """Serialized a list of workTask objects.

        Args:
            workTaskObjects - A list of workPlace ORM objects.
            deref - A list of fields to deref.

        Returns:
            A list of serialized WorkTask JSON objects.
        """
        pass