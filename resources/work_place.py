from dbmodels import models
from collections import OrderedDict
from flask import jsonify

from lib import status

DEREF_LIST = ['user', 'tasks', 'address']

class Workplace(object):
    """Workplace resources.
    """
    @classmethod
    def get(cls, workPlaceId, deref=[]):
        """Get workPlace by workPlaceId.

        Args:
            workPlaceId - A specified workPlace Id.
            deref - A list of fields to deref.

        Returns:
            A serialized WorkPlace JSON dict.
        """
        cls.__validateDeref(deref)
        workPlace = models.WorkPlace.query.get(workPlaceId)

        if not workPlace:
            raise status.ResourceNotFound('WorkPlace', resourceId=workPlaceId)

        return cls.__to_Dict([workPlace], deref)[0]

    @classmethod
    def find(cls, name=None, initial=None, positionTitle=None,
             deref=[]):
        """Find workPlaces that meet the expected query parameters.

        Args:
            name - The name of the company.
            initial - The initial of the company.
            positionTitle - The position title.

        Returns:
            A list of matched and serialized WorkPlace objects.
        """
        cls.__validateDeref(deref)
        query_params = {
            'name': name,
            'initial': initial,
            'position_title': positionTitle
        }

        for field in ['name', 'initial', 'position_title']:
            if query_params[field] is None:
                del query_params[field]

        workPlaces = models.WorkPlace.query.filter_by(**query_params).all()

        if not workPlaces:
            raise status.ResourceNotFound('WorkPlace', query_params=query_params)

        return cls.__to_Dict(workPlaces, deref)

    @classmethod
    def update(cls, workPlaceId, **kwargs):
        """Update specified workPlace with given arguments. 
        """
        raise NotImplementedError('WorkPlace Resource - update method is currently '
                                  'not supported.')

    @classmethod
    def create(cls, name=None, initial=None, positionTitle=None, startDate=None,
               endDate=None, addressId=None, userId=1):
        """Create a new workPlace entry.
        """
        raise NotImplementedError('WorkPlace Resource - create method is currently '
                                  'not supported.')

    @classmethod
    def __validateDeref(cls, derefList):
        """Validate the deref list in the query string.
        """
        for deref in derefList:
            if deref not in DEREF_LIST:
                derefList.remove(deref)

    @classmethod
    def __to_Dict(cls, workPlaceObjects, deref):
        """Serialized a list of workPlace objects.

        Args:
            workPlaceObjects - A list of workPlace ORM objects.
            deref - A list of fields to deref.

        Returns:
            A list of serialized WorkPlace JSON objects.
        """
        def formatDate(dateTime):
            return str(dateTime.month) + '/' + str(dateTime.year)

        workPlaceDicts = []
        for workPlace in workPlaceObjects:
            workPlaceDict = OrderedDict([
                ('id', workPlace.id),
                ('name', workPlace.name),
                ('initial', workPlace.initial),
                ('positionTitle', workPlace.position_title),
                ('startDate', formatDate(workPlace.start_date)),
                ('endDate', formatDate(workPlace.end_date))
            ])

            if 'user' in deref:
                user = workPlace.employee.email
                workPlaceDict['user'] = user

            if 'tasks' in deref:
                workTasks = dict((k, v.description) for k, v in
                                  enumerate(workPlace.work_tasks, start=1))
                workPlaceDict['tasks'] = workTasks

            if 'address' in deref:
                pass

            workPlaceDicts.append(workPlaceDict)

        return workPlaceDicts
