from collections import OrderedDict

from dbmodels import models
from lib import status as custom_status, validation

DEREF_LIST = ['skill']

class Tag(object):
    """Tag resources.
    """
    @classmethod
    def get(cls, tagId, deref=[]):
        """
        """
        validation.validateDeref(DEREF_LIST, deref)
        tag = models.Tag.query.get(tagId)

        if not tag:
            raise custom_status.ResourceNotFound(msg='No tag found with Id - %s' %
                                                 tagId)

        return cls._to_Dict([tag], deref)

    @classmethod
    def find(cls, name=None, deref=[]):
        """
        """
        validation.validateDeref(DEREF_LIST, deref)
        query_params = {}
        if name:
            query_params['name'] = name

        tags = models.Tag.query.filter_by(**query_params).all()

        if not tags:
            raise custom_status.ResourceNotFound(msg='No tags found with given '
                                                 'query parameters',
                                                 details=query_params)

        return cls._to_Dict(tags, deref)

    @classmethod
    def update(cls, tagId, **kwargs):
        """Update specified tag with given arguments.
        """
        raise NotImplementedError('Tag Resource - update method is currently '
                                  'not supported.')

    @classmethod
    def create(cls, name, **kwargs):
        """Create a new Tag entry.
        """
        raise NotImplementedError('Tag Resource - create method is currently '
                                  'not supported.')

    @classmethod
    def _to_Dict(cls, tagObjects, deref):
        """Serialized a list of Tag objects.

        Args:
            tagObjects - A list of tag ORM objects.
            deref - A list of fields to deref.

        Returns:
            A list of serialized tag JSON objects.
        """
        tagDicts = []
        for tag in tagObjects:
            tagDict = OrderedDict([
                ('id', tag.id),
                ('tagName', tag.name)
            ])

            if 'skill' in deref:
                skills = tag.skills.all()
                if skills and isinstance(skills, list):
                    # Import here to avoid circular import.
                    from resources.skill import Skill
                    tagDict['skills'] = Skill._to_Dict(skills, deref=[])

            tagDicts.append(tagDict)

        return tagDicts
