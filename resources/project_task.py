from collections import OrderedDict

from dbmodels import models
from lib import status as custom_status

DEREF_LIST = ['project']

class ProjectTask(object):
    """Projecttask resources.
    """
    @classmethod
    def get(cls, projectTaskId, deref=[]):
        """Get ProjectTask by projectTaskId.

        Args:
            projectTaskId - A specified ProjectTask Id.
            deref - A list of fields to deref.

        Returns:
            A serialized ProjectTask JSON dict.
        """
        cls.__validateDeref(deref)
        projectTask = models.ProjectTask.query.get(projectTaskId)

        if not projectTask:
            raise custom_status.ResourceNotFound(msg='No projectTask found with Id '
                                                '- %s' % projectTaskId)

        return cls._to_Dict([projectTask], deref)[0]

    @classmethod
    def find(cls, projectName=None, deref=[]):
        """Find ProjectTasks that meet the expected query parameters.

        Args:
            projectName - The name of the project.

        Returns:
            A list of matched and serialized ProjectTask objects.
        """
        cls.__validateDeref(deref)
        query_params = {
            'name': projectName
        }

        for field in query_params.keys():
            if query_params[field] is None:
                del query_params[field]

        projects = models.Project.query.filter_by(**query_params).all()

        if not projects:
            raise custom_status.ResourceNotFound(msg='No projectTask found with given '
                                                 'query parameters',
                                                 details=query_params)

        projectTasks = []
        for project in projects:
            projectTasks += project.project_tasks

        return cls._to_Dict(projectTasks, deref)

    @classmethod
    def update(cls, projectTaskId, **kwargs):
        """Update specified ProjectTask with given arguments.
        """
        raise NotImplementedError('ProjectTask Resource - update method is currently '
                                  'not supported.')

    @classmethod
    def create(cls, description=None, project_id=None):
        """Create a new ProjectTask entry.
        """
        raise NotImplementedError('ProjectTask Resource - create method is currently '
                                  'not supported.')

    @classmethod
    def __validateDeref(cls, derefList):
        """Validate the deref list in the query string.
        """
        for deref in list(derefList):
            if deref not in DEREF_LIST:
                derefList.remove(deref)

    @classmethod
    def _to_Dict(cls, projectTaskObjects, deref):
        """Serialized a list of ProjectTask objects.

        Args:
            projectTaskObjects - A list of ProjectTask ORM objects.
            deref - A list of fields to deref.

        Returns:
            A list of serialized ProjectTask JSON objects.
        """
        projectCache = {}
        projectTaskDicts = []
        for projectTask in projectTaskObjects:
            projectTaskDict = OrderedDict([
                ('id', projectTask.id),
                ('description', projectTask.description)
            ])

            if 'project' in deref:
                if projectTask.project_id not in projectCache:
                    projectCache.update({
                        projectTask.project_id: projectTask.project.name
                    })

                projectTaskDict['project'] = projectCache[projectTask.project_id]

            projectTaskDicts.append(projectTaskDict)

        return projectTaskDicts
