from collections import OrderedDict

from dbmodels import models
from lib import status as custom_status, validation
from resources.tag import Tag

DEREF_LIST = ['tag', 'user']

class Skill(object):
    """Skill resources.
    """
    @classmethod
    def get(cls, skillId, deref=[]):
        """Get skill by skillId.

        Args:
            skillId - A specified skill Id.
            deref - A list of fields to deref.

        Returns:
            A serialized skill JSON dict.
        """
        deref = validation.validateDeref(DEREF_LIST, deref)
        skill = models.Skill.query.get(skillId)

        if not skill:
            raise custom_status.ResourceNotFound(msg='No skill found with Id - %s' %
                                                 skillId)

        return cls._to_Dict([skill], deref)

    @classmethod
    def find(cls, description=None, tag=None, userId=None, deref=[]):
        """Find skills that meet the expected query parameters.

        Args:
            description - The description of the skill.
            tag - The name of the tag that is associated to the skill.
            userId - The Id of the user.

        Returns:
            A list of serialized skill JSON dicts.
        """
        deref = validation.validateDeref(DEREF_LIST, deref)
        query_params = {
            'user_id': userId,
            'description': description
        }

        if tag:
            tags = Tag.find(name=tag)
            tagId = tags[0]['id'] if tags else None
            query_params['tag_id'] = tagId


        for field in query_params.keys():
            if not query_params[field]:
                del query_params[field]

        skills = models.Skill.query.filter_by(**query_params).all()

        if not skills:
            raise custom_status.ResourceNotFound(msg='No skills found with given '
                                                 'query parameters',
                                                 details=query_params)

        return cls._to_Dict(skills, deref)

    @classmethod
    def update(cls, skillId, **kwargs):
        """Update specified user with given arguments.
        """
        raise NotImplementedError('Skill Resource - update method is currently '
                                  'not supported.')

    @classmethod
    def create(cls, description, **kwargs):
        """Create a new project entry.
        """
        raise NotImplementedError('Skill Resource - create method is currently '
                                  'not supported.')

    @classmethod
    def _to_Dict(cls, skillObjects, deref):
        """Serialized a list of Skill objects.

        Args:
            skillObjects - A list of Skill ORM objects.
            deref - A list of fields to deref.

        Returns:
            A list of serialized skill JSON objects.
        """
        skillDicts = []
        for skill in skillObjects:
            skillDict = OrderedDict([
                ('id', skill.id),
                ('description', skill.description)
            ])

            if 'user' in deref:
                skillDict['user'] = skill.possessor.email

            if 'tag' in deref:
                skillDict['tag'] = skill.tag.name

            skillDicts.append(skillDict)

        return skillDicts
