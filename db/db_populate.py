import sys

from default_config import *
from app import db, models

class Populate(object):
    """Populate class which contains methods to pre-insert meta data to database.  
    """
    @classmethod
    def user(cls):
        for user in USER_LIST.values():
            entry = models.User(**user)
            db.session.add(entry)

    @classmethod
    def workPlace(cls):
        for workplace in WORKPLACE_LIST.values():
            entry = models.WorkPlace(**workplace)
            db.session.add(entry)

    @classmethod
    def workTask(cls):
        for k, v in WORKTASK_LIST.iteritems():
            for task in v:
                entry = {
                    'description': task,
                    'workplace_id': WORKPLACE_LIST[k]['id']
                }
                entry = models.WorkTask(**entry)
                db.session.add(entry)

    @classmethod
    def address(cls):
        """Generate addresses and insert them into database.
        """
        for address in ADDRESS_LIST.values():
            entry = models.Address(**address)
            db.session.add(entry)

    @classmethod
    def tag(cls):
        """Generate a list of tags and insert them into database.
        """
        for tag in TAGS_LIST:
            tag = models.Tag(name=tag)
            db.session.add(tag)

    @classmethod
    def skill(cls):
        """Generate skills and attach them with specific user and tag, then insert
        them into database.
        """
        tag_id_mapping = dict((v, k) for k, v in enumerate(TAGS_LIST, start=1))
        tag_skills_mapping = {
            'Python': [PYTHON_LIST],
            'Ruby on Rails': [RUBY_LIST],
            'C++/C': [C_LIST, CPP_LIST],
            'Others': [OTHER_LIST],
            'Database': [DATABASE_LIST],
            'Server': [SERVER_LIST],
            'Cloud': [CLOUD_LIST],
            'Tools': [TOOLS_LIST]
        }

        for tag, skills in tag_skills_mapping.iteritems():
            for i in skills:
                for item in i:
                    item_kargs = {
                        'description': item,
                        'tag_id': tag_id_mapping[tag],
                        'user_id': 1
                    }
                    item = models.Skill(**item_kargs)
                    db.session.add(item)

    @classmethod
    def school(cls):
        for school in SCHOOL_LIST.values():
            entry = models.School(**school)
            db.session.add(entry)

    @classmethod
    def course(cls):
        pass

    @classmethod
    def project(cls):
        for project in PROJECT_LIST.values():
            entry = models.Project(**project)
            db.session.add(entry)

    @classmethod
    def projectTask(cls):
        for k, v in PROJECTTASK_LIST.iteritems():
            for task in v:
                entry = {
                    'description': task,
                    'project_id': PROJECT_LIST[k]['id']
                }
                entry = models.ProjectTask(**entry)
                db.session.add(entry)

class RebuildDB(object):
    """RebuildDB class which contains methods to rebuild database with predefied
    data.
    """
    TABLES = ['User', 'WorkPlace', 'WorkTask', 'Address', 'Tag', 'Skill', 'School',
              'Course', 'Project', 'ProjectTask']

    @classmethod
    def _purgeTables(cls):
        """Delete entries from all tables in the database.
        """
        for table in cls.TABLES:
            table = getattr(models, table)
            print 'Deleting %s table ...' % table.__name__
            table.query.delete()

        db.session.commit()

    @classmethod
    def _populateTables(cls):
        """Insert entries with predefined data into the databse.
        """
        for method in dir(Populate):
            if not method.startswith('__'):
                populateTable = getattr(Populate, method)
                print 'Inserting data into %s table ...' % method
                populateTable()

        db.session.commit()

    @classmethod
    def initiate(cls):
        """Initiate a new database. It will purge all tables and build new ones.
        """
        cls._purgeTables()
        cls._populateTables()
        print 'DB initialization finished!!'

def main():
    RebuildDB.initiate()
    return 0

if __name__ == '__main__':
    sys.exit(main())
