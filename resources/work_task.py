from collections import OrderedDict

from dbmodels import models
from lib import status as custom_status, validation

DEREF_LIST = ['workplace']

class Worktask(object):
    """Worktask resources.
    """
    @classmethod
    def get(cls, workTaskId, deref=[]):
        """Get WorkTask by workTaskId.

        Args:
            workTaskId - A specified WorkTask Id.
            deref - A list of fields to deref.

        Returns:
            A serialized WorkTask JSON dict.
        """
        deref = validation.validateDeref(DEREF_LIST, deref)
        workTask = models.WorkTask.query.get(workTaskId)

        if not workTask:
            raise custom_status.ResourceNotFound(msg='No workTask found with Id - %s'
                                                 % workTaskId)

        return cls._to_Dict([workTask], deref)[0]

    @classmethod
    def find(cls, workPlaceName=None, initial=None, deref=[]):
        """Find WorkTasks that meet the expected query parameters.

        Args:
            workPlaceName - The name of the company.

        Returns:
            A list of matched and serialized WorkTask objects.
        """
        deref = validation.validateDeref(DEREF_LIST, deref)
        query_params = {
            'name': workPlaceName,
            'initial': initial
        }

        for field in query_params.keys():
            if query_params[field] is None:
                del query_params[field]

        workPlaces = models.WorkPlace.query.filter_by(**query_params).all()

        if not workPlaces:
            raise custom_status.ResourceNotFound(msg='No workTask found with given '
                                                 'query parameters',
                                                 details=query_params)

        workTasks = []
        for workPlace in workPlaces:
            workTasks += workPlace.work_tasks

        return cls._to_Dict(workTasks, deref)

    @classmethod
    def update(cls, workTaskId, **kwargs):
        """Update specified WorkTask with given arguments.
        """
        raise NotImplementedError('WorkTask Resource - update method is currently '
                                  'not supported.')

    @classmethod
    def create(cls, description, workplaceId=None):
        """Create a new WorkTask entry.
        """
        raise NotImplementedError('WorkTask Resource - create method is currently '
                                  'not supported.')

    @classmethod
    def _to_Dict(cls, workTaskObjects, deref):
        """Serialized a list of WorkTask objects.

        Args:
            workTaskObjects - A list of WorkTask ORM objects.
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
