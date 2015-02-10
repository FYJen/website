import datetime
from collections import OrderedDict

from dbmodels import models
from lib import status as custom_status, validation
from resources.address import Address

DEREF_LIST = ['user', 'tasks', 'address']

class Workplace(object):
    """Workplace resources.
    """
    @classmethod
    def get(cls, workPlaceId, deref=[]):
        """Get WorkPlace by workPlaceId.

        Args:
            workPlaceId - A specified WorkPlace Id.
            deref - A list of fields to deref.

        Returns:
            A serialized WorkPlace JSON dict.
        """
        deref = validation.validateDeref(DEREF_LIST, deref)
        workPlace = models.WorkPlace.query.get(workPlaceId)

        if not workPlace:
            raise custom_status.ResourceNotFound(msg='No workPlace found with Id - %s'
                                                 % workPlaceId)

        return cls._to_Dict([workPlace], deref)[0]

    @classmethod
    def find(cls, name=None, initial=None, positionTitle=None,
             deref=[]):
        """Find WorkPlaces that meet the expected query parameters.

        Args:
            name - The name of the company.
            initial - The initial of the company.
            positionTitle - The position title.

        Returns:
            A list of matched and serialized WorkPlace objects.
        """
        deref = validation.validateDeref(DEREF_LIST, deref)
        query_params = {
            'name': name,
            'initial': initial,
            'position_title': positionTitle
        }

        for field in query_params.keys():
            if query_params[field] is None:
                del query_params[field]

        workPlaces = models.WorkPlace.query.filter_by(**query_params).all()

        if not workPlaces:
            raise custom_status.ResourceNotFound(msg='No workPlaces found with '
                                                 'given query parameters',
                                                 details=query_params)

        return cls._to_Dict(workPlaces, deref)

    @classmethod
    def update(cls, workPlaceId, **kwargs):
        """Update specified WorkPlace with given arguments.
        """
        raise NotImplementedError('WorkPlace Resource - update method is currently '
                                  'not supported.')

    @classmethod
    def create(cls, name, positionTitle, **kwargs):
        """Create a new WorkPlace entry.
        """
        raise NotImplementedError('WorkPlace Resource - create method is currently '
                                  'not supported.')

    @classmethod
    def _to_Dict(cls, workPlaceObjects, deref):
        """Serialized a list of WorkPlace objects.

        Args:
            workPlaceObjects - A list of WorkPlace ORM objects.
            deref - A list of fields to deref.

        Returns:
            A list of serialized WorkPlace JSON objects.
        """
        def formatDate(dateTime):
            try:
                now = datetime.datetime.today()
                return_val = str(dateTime.month) + '/' + str(dateTime.year) if \
                              dateTime < now else 'Present'
                return return_val
            except Exception:
                return None

        workPlaceDicts = []
        for workPlace in workPlaceObjects:
            workPlaceDict = OrderedDict([
                ('id', workPlace.id),
                ('name', workPlace.name),
                ('initial', workPlace.initial),
                ('positionTitle', workPlace.position_title),
                ('startDate', formatDate(workPlace.start_date)),
                ('endDate', formatDate(workPlace.end_date)),
                ('web_link', workPlace.web_link)
            ])

            if 'user' in deref:
                workPlaceDict['user'] = workPlace.employee.email

            if 'tasks' in deref:
                workPlaceDict['tasks'] = [workTask.description for workTask in
                                          workPlace.work_tasks]

            if 'address' in deref:
                workPlaceDict['address'] = \
                    Address._to_Dict([workPlace.address], True, [])

            workPlaceDicts.append(workPlaceDict)

        return workPlaceDicts
