from default_config import *

from app import db, models

class Populate(object):
    """Populate class which contains methods to pre-insert meta data to database.  
    """
    @classmethod
    def user(cls):
        for k, v in USER_LIST.iteritems():
            k = models.User(**v)
            db.session.add(k)

        db.session.commit()

    @classmethod
    def workPlace(cls):
        for k, v in WORKPLACE_LIST.iteritems():
            k = models.WorkPlace(**v)
            db.session.add(k)

        db.session.commit()

    @classmethod
    def workTask(cls):
        pass

    @classmethod
    def address(cls):
        """Generate addresses and insert them into database.
        """
        for k, v in ADDRESS_LIST.iteritems():
            k = models.Address(**v)
            db.session.add(k)

        db.session.commit()

    @classmethod
    def tag(cls):
        """Generate a list of tags and insert them into database.
        """
        for tag in TAGS_LIST:
            tag = models.Tag(name=tag)
            db.session.add(tag)
        db.session.commit()

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

        db.session.commit()

    @classmethod
    def school(cls):
        pass

    @classmethod
    def course(cls):
        pass

    @classmethod
    def project(cls):
        pass

def _purgeTables():
    """Delete all entries from all tables in the database.
    """
    for table in ['User', 'WorkPlace', 'WorkTask', 'Address', 'Tag', 'Skill',
                  'School', 'Course', 'Project']:
        table = getattr(models, table)
        table.query.delete()

    db.session.commit()

def main():
    pass

if __name__ == '__main__':
    _purgeTables()
    Populate.address()
    Populate.user()
    Populate.tag()
    Populate.skill()
    Populate.workPlace()