import datetime
from collections import OrderedDict

from dbmodels import models
from lib import status as custom_status, validation
from resources.address import Address

DEREF_LIST = ['address', 'course']

class School(object):
    """School resources.
    """
    @classmethod
    def get(cls, schoolId, deref=[]):
        """Get School by schoolId.

        Args:
            schoolId - A specified School Id.
            deref - A list of fields to deref.

        Returns:
            A serialized School JSON dict.
        """
        deref = validation.validateDeref(DEREF_LIST, deref)
        school = models.School.query.get(schoolId)

        if not school:
            raise custom_status.ResourceNotFound(msg='No School found with Id - %s' \
                                                 % schoolId)

        return cls._to_Dict([school], deref)

    @classmethod
    def find(cls, name=None, level=None, attending=None, deref=[]):
        """Find Address that meet the expected query parameters.

        Args:
            name - The name of the school.
            level - Education level.
            attending - True if still attending else False.

        Returns:
            A list of serialized School objects.
        """
        def convertToBoolean(strBoolean):
            retVal = None
            if strBoolean.lower() == 'true':
                retVal = True
            elif strBoolean.lower() == 'false':
                retVal = False
            else:
                raise custom_status.InvalidRequest(details='stringBoolean should '
                                                   'be either \'true\' or \'false\'')
            
            return retVal

        deref = validation.validateDeref(DEREF_LIST, deref)
        query_params = {
            'name': name,
            'level': level,
            'attending': convertToBoolean(attending) if attending else None
        }

        for field in query_params.keys():
            if query_params[field] in [None, '']:
                del query_params[field]

        schools = models.School.query.filter_by(**query_params).all()

        if not schools:
            raise custom_status.ResourceNotFound(msg='No School found with the '
                                                 'given query parameters',
                                                 details=query_params)

        return cls._to_Dict(schools, deref)

    @classmethod
    def update(cls, addressId, **kwargs):
        """Update specified School with given arguments.
        """
        raise NotImplementedError('School Resource - update method is currently '
                                  'not supported.')

    @classmethod
    def create(cls, name=None, degree=None, major=None, minor=None, joint=None,
               level=None, start_date=None, end_date=None, attending=True,
               term=None):
        """Create a new School entry.
        """
        raise NotImplementedError('School Resource - create method is currently '
                                  'not supported.')

    @classmethod
    def _to_Dict(cls, schoolObjects, deref):
        """Serialize a list of School objects.

        Args:
            schoolObjects - A list of School ORM objects.
            deref - A list of fields to deref.

        Returns:
            A list of serialized School JSON objects.
        """
        def formatDate(dateTime):
            try:
                now = datetime.datetime.today()
                return_val = str(dateTime.month) + '/' + str(dateTime.year) if \
                              dateTime < now else 'Present'
                return return_val
            except Exception:
                return None

        schoolDicts = []
        for school in schoolObjects:
            schoolDict = OrderedDict([
                ('id', school.id),
                ('name', school.name),
                ('level', school.level),
                ('degree', school.degree),
                ('major', school.major),
                ('minor', school.minor),
                ('joint', school.joint),
                ('startDate', formatDate(school.start_date)),
                ('endDate', formatDate(school.end_date)),
                ('attending', school.attending),
                ('term', school.term),
            ])

            if 'address' in deref:
                schoolDict['address'] = \
                    Address._to_Dict([school.address], True, [])

            if 'course' in deref:
                pass

            schoolDicts.append(schoolDict)

        return schoolDicts