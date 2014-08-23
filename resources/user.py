from collections import OrderedDict

from dbmodels import models
from lib import status as custom_status, validation
from resources.work_place import Workplace
from resources.project import Project
from resources.address import Address

DEREF_LIST = ['workPlaces', 'skills', 'projects', 'schools', 'address']

class User(object):
    """User resources.
    """
    @classmethod
    def get(cls, userId, deref=[]):
        """Get user by userId.

        Args:
            userId - A specified user Id.
            deref - A list of fields to deref.

        Returns:
            A serialized user JSON dict.
        """
        deref = validation.validateDeref(DEREF_LIST, deref)
        user = models.User.query.get(userId)

        if not user:
            raise custom_status.ResourceNotFound(msg='No user found with Id - %s' %
                                                 userId)

        return cls._to_Dict([user], deref)[0]

    @classmethod
    def find(cls, email=None, firstName=None, lastName=None, phone=None, deref=[]):
        """Find users that meet the expected query parameters.

        Args:
            email - The email of the user.
            firstName - The firstName of the user.
            lastName - The lastName of the user.
            phone - The phone of the users.
            deref - A list of fields to deref.
        """
        deref = validation.validateDeref(DEREF_LIST, deref)
        query_params = {
            'email': email,
            'first_name': firstName,
            'last_name': lastName,
            'phone': phone
        }

        for field in query_params.keys():
            if not query_params[field]:
                del query_params[field]

        users = models.User.query.filter_by(**query_params).all()

        if not users:
            raise custom_status.ResourceNotFound(msg='No users found with given '
                                                 'query parameters',
                                                 details=query_params)

        return cls._to_Dict(users, deref)

    @classmethod
    def update(cls, projectId, **kwargs):
        """Update specified user with given arguments.
        """
        raise NotImplementedError('User Resource - update method is currently '
                                  'not supported.')

    @classmethod
    def create(cls, name=None, initial=None, positionTitle=None, startDate=None,
               endDate=None, addressId=None, userId=1):
        """Create a new project entry.
        """
        raise NotImplementedError('User Resource - create method is currently '
                                  'not supported.')

    @classmethod
    def _to_Dict(cls, userObjects, deref):
        """Serialized a list of User objects.

        Args:
            userObjects - A list of User ORM objects.
            deref - A list of fields to deref.

        Returns:
            A list of serialized user JSON objects.
        """
        userDicts = []
        for user in userObjects:
            userDict = OrderedDict([
                ('id', user.id),
                ('name', (' ').join([user.first_name, user.last_name])),
                ('email', user.email),
                ('phone', user.phone),
                ('github', user.github),
                ('linkedin', user.linkedin)
            ])

            if 'address' in deref:
                addresses = user.address
                if addresses:
                    userDict['address'] = Address._to_Dict([addresses], True,
                                                           deref=[])

            if 'workPlaces' in deref:
                workPlaces = user.workPlaces.all()
                if workPlaces and isinstance(workPlaces, list):
                    userDict['workExperiences'] = \
                        Workplace._to_Dict(workPlaces, deref=['tasks', 'address'])

            if 'projects' in deref:
                projects = user.projects.all()
                if projects and isinstance(projects, list):
                    userDict['projects'] = Project._to_Dict(projects,
                                                            deref=['tasks'])

            if 'skills' in deref:
                pass

            if 'schools' in deref:
                pass

            userDicts.append(userDict)

        return userDicts
