from collections import OrderedDict

from dbmodels import models
from lib import status as custom_status

DEREF_LIST = ['occupants']

class Address(object):
    """Address resources.
    """
    @classmethod
    def get(cls, addressId, stringlized=False, deref=[]):
        """Get Address by addressId.

        Args:
            addressId - A specified Address Id.
            stringlized - Whether to flatten addresses.
            deref - A list of fields to deref.

        Returns:
            A serialized Address JSON dict.
        """
        cls.__validateDeref(deref)
        address = models.Address.query.get(addressId)

        if not address:
            raise custom_status.ResourceNotFound(msg='No Address found with Id - %s' \
                                                 % addressId)

        return cls._to_Dict([address], stringlized, deref)[0]

    @classmethod
    def find(cls, active=None, country=None, postalCode=None, zipCode=None,
             stringlized=False, deref=[]):
        """Find Addresses that meet the expected query parameters.

        Args:
            active - Whether the Address needs to be active or not.
            country - The country of the Address.
            postalCode - The postal code of the Address if in Canada.
            zip - The zip code of the Address if in USA.
            stringlized - Whether to flatten addresses.
            deref - A list of fields to deref.

        Returns:
            A list of matched and serialized Address objects.
        """
        cls.__validateDeref(deref)
        if postalCode and zipCode:
            raise custom_status.InvalidRequest(msg='Cannot specify postalCode and '
                                              'zipCode together')

        query_params = {
            'active': active,
            'country': country,
            'postalcode_zip': (postalCode or zipCode)
        }
        for field in query_params.keys():
            if query_params[field] is None:
                del query_params[field]

        addresses = models.Address.query.filter_by(**query_params).all()

        if not addresses:
            raise custom_status.ResourceNotFound(msg='No address found with the '
                                                'given query parameters',
                                                details=query_params)

        return cls._to_Dict(addresses, stringlized, deref)

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
            stringlized - Whether to flatten addresses.
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
                ('occupants', set())
            ])

            if 'occupants' in deref:
                for possibleOccupant in ['users', 'school', 'workPlace']:
                    result = getattr(address, possibleOccupant)
                    if isinstance(result, list):
                        for occupant in result:
                            addressDict['occupants'].add(occupant.email)
                    elif result:
                        addressDict['occupants'].add(result.name)

            # Since set object is not JSON serializable, we covnert it to list
            # object.
            addressDict['occupants'] = list(addressDict['occupants'])

            if stringlized:
                addressDict['stringlizedAddr'] = stringlizedAddress(addressDict)

            addressDicts.append(addressDict)

        return addressDicts
