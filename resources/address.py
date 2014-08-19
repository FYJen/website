from collections import OrderedDict

from dbmodels import models
from lib import status as custom_status

DEREF_LIST = ['users', 'work_place', 'school']

class Address(object):
    """Address resources.
    """
    @classmethod
    def get(cls, addressId, stringlized=False, deref=[]):
        """Get Address by addressId.

        Args:
            addressId - A specified Address Id.
            deref - A list of fields to deref.

        Returns:
            A serialized Address JSON dict.
        """
        cls.__validateDeref(deref)
        address = models.Address.query.get(addressId)

        if not address:
            raise custom_status.ResourceNotFound('Address', resourceId=addressId)

        return cls._to_Dict([address], stringlized, deref)[0]

    @classmethod
    def find(cls, active=None, country=None, postalCode=None, zip=None):
        """Find Addresses that meet the expected query parameters.

        Args:
            active - Whether the Address needs to be active or not.
            country - The country of the Address.
            postalCode - The postal code of the Address if in Canada.
            zip - The zip code of the Address if in USA.

        Returns:
            A list of matched and serialized Address objects.
        """
        pass

    @classmethod
    def update(cls, addressId, **kwargs):
        """Update specified Address with given arguments.
        """
        raise NotImplementedError('Address Resource - update method is currently '
                                  'not supported.')

    @classmethod
    def create(cls, apt_number=None, suite_number=None, floor=None,
               street_name=None, city=None, province_state=None, country=None,
               postalcode_zip=None, active=None):
        """Create a new Address entry.
        """
        raise NotImplementedError('Address Resource - create method is currently '
                                  'not supported.')

    @classmethod
    def __validateDeref(cls, derefList):
        """Validate the deref list in the query string.
        """
        for deref in derefList:
            if deref not in DEREF_LIST:
                derefList.remove(deref)

    @classmethod
    def _to_Dict(cls, addressObjects, stringlized, deref):
        """Serialized a list of Address objects.

        Args:
            addressObjects - A list of Address ORM objects.
            deref - A list of fields to deref.

        Returns:
            A list of serialized WorkPlace JSON objects.
        """
        def stringlizedAddress(addressObj):
            addressStr = []

            for field in ['Apt/Suite/Floor', 'streetName', 'city', 'province/state',
                          'country', 'postalCode/zip']:
                if addressObj[field]:
                    addressStr.append(addressObj[field])

            return (', ').join(addressStr)

        addressDicts = []
        for address in addressObjects:
            addressDict = OrderedDict([
                ('id', address.id),
                ('Apt/Suite/Floor', (address.apt_number or address.suite_number or
                                     address.floor or '')),
                ('streetName', address.street_name),
                ('city', address.city),
                ('province/state', address.province_state),
                ('country', address.country),
                ('postalCode/zip', address.postalcode_zip),
                ('active', address.active),
                ('currentOwnerOrTenants', [])
            ])

            if 'users' in deref:
                for user in address.users:
                    addressDict['currentOwnerOrTenants'].append(user.email)

            if 'school' in deref:
                addressDict['currentOwnerOrTenants'].append(address.school.name)

            if 'workPlace' in deref:
                addressDict['currentOwnerOrTenants'].append(address.workPlace.name)

            if stringlized:
                addressDict['stringlizedAddr'] = stringlizedAddress(addressDict)

            addressDicts.append(addressDict)

        return addressDicts
