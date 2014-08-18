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
    def find(cls, workPlaceName=None, initial=None, deref=[]):
        """Find workTasks that meet the expected query parameters.

        Args:
            workPlaceName - The name of the company.

        Returns:
            A list of matched and serialized WorkTask objects.
        """
        cls.__validateDeref(deref)
        query_params = {
            'name': workPlaceName,
            'initial': initial
        }

        for field in ['name', 'initial']:
            if query_params[field] is None:
                del query_params[field]
        
        workPlaceIds = [workPlace.id for workPlace in
                        models.WorkPlace.query.filter_by(**query_params).all()]

        if not workPlaceIds:
            raise status.ResourceNotFound('WorkTask', workPlaceName=workPlaceName)

        workTasks = models.WorkTask.query.filter(models.WorkTask.workplace_id \
                    .in_(workPlaceIds)).all()

        if not workTasks:
            raise status.ResourceNotFound('WorkTask', details='The given '
                                          'workPlaceName - %s, does not contain any '
                                          'task' % workPlaceName)

        return cls.__to_Dict(workTasks, deref)

    @classmethod
    def update(cls, workTaskId, **kwargs):
        """Update specified workTask with given arguments. 
        """
        raise NotImplementedError('WorkTask Resource - update method is currently '
                                  'not supported.')

    @classmethod
    def create(cls, description=None, workplace_id=None):
        """Create a new workTask entry.
        """
        raise NotImplementedError('WorkTask Resource - create method is currently '
                                  'not supported.')

    @classmethod
    def __validateDeref(cls, derefList):
        """Validate the deref list in the query string.
        """
        for deref in list(derefList):
            if deref not in DEREF_LIST:
                derefList.remove(deref)

    @classmethod
    def __to_Dict(cls, workTaskObjects, deref):
        """Serialized a list of workTask objects.

        Args:
            workTaskObjects - A list of workTask ORM objects.
            deref - A list of fields to deref.

        Returns:
            A list of serialized WorkTask JSON objects.
        """
        workPlaceCache = {}
        workTaskDicts = []
        for workTask in workTaskObjects:
            workTaskDict = OrderedDict([
                ('id', workTask.id),
                ('description', workTask.description)
            ])

            if 'workplace' in deref:
                if workTask.workplace_id not in workPlaceCache:
                    workPlaceCache.update({
                        workTask.workplace_id: workTask.workplace.name
                    })
                
                workTaskDict['workPlace'] = workPlaceCache[workTask.workplace_id]

            workTaskDicts.append(workTaskDict)

        return workTaskDicts
