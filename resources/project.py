from collections import OrderedDict

from dbmodels import models
from lib import status as custom_status, validation

DEREF_LIST = ['tasks', 'user']

class Project(object):
    """Project resources.
    """
    @classmethod
    def get(cls, projectId, deref=[]):
        """Get project by projectId.

        Args:
            projectId - A specified project Id.
            deref - A list of fields to deref.

        Returns:
            A serialized project JSON dict.
        """
        deref = validation.validateDeref(DEREF_LIST, deref)
        project = models.Project.query.get(projectId)

        if not project:
            raise custom_status.ResourceNotFound(msg='No project found with Id - %s'
                                                 % projectId)

        return cls._to_Dict([project], deref)[0]

    @classmethod
    def find(cls, projectName=None, deref=[]):
        """Find projects that meet the expected query parameters.

        Args:
            projectName - The name of the project.

        Returns:
            A list of matched and serialized project objects.
        """
        deref = validation.validateDeref(DEREF_LIST, deref)
        query_params = {
            'name': projectName
        }

        for field in query_params.keys():
            if query_params[field] is None:
                del query_params[field]

        projects = models.Project.query.filter_by(**query_params).all()

        if not projects:
            raise custom_status.ResourceNotFound(msg='No projects found with '
                                                 'given query parameters',
                                                 details=query_params)

        return cls._to_Dict(projects, deref)

    @classmethod
    def update(cls, projectId, **kwargs):
        """Update specified project with given arguments.
        """
        raise NotImplementedError('Project Resource - update method is currently '
                                  'not supported.')

    @classmethod
    def create(cls, name=None, initial=None, positionTitle=None, startDate=None,
               endDate=None, addressId=None, userId=1):
        """Create a new project entry.
        """
        raise NotImplementedError('Project Resource - create method is currently '
                                  'not supported.')

    @classmethod
    def _to_Dict(cls, projectObjects, deref):
        """Serialized a list of Project objects.

        Args:
            projectObjects - A list of project ORM objects.
            deref - A list of fields to deref.

        Returns:
            A list of serialized project JSON objects.
        """
        def formatDate(dateTime):
            try:
                return str(dateTime.month) + '/' + str(dateTime.year)
            except Exception:
                return None

        projectDicts = []
        for project in projectObjects:
            projectDict = OrderedDict([
                ('id', project.id),
                ('name', project.name),
                ('startDate', formatDate(project.start_date)),
                ('endDate', formatDate(project.end_date)),
                ('thumbnail', project.thumbnail)
            ])

            if 'user' in deref:
                projectDict['user'] = project.owner.email

            if 'tasks' in deref:
                projectDict['tasks'] = [projectTask.description for projectTask in
                                        project.project_tasks]

            projectDicts.append(projectDict)

        return projectDicts
