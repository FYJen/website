from app import db, models

class Populate(object):
    """Populate class which contains methods to pre-insert meta data to database.  
    """
    @classmethod
    def user(cls):
        user_kwargs = {
            'first_name': 'Fei-Yang',
            'last_name': 'Jen',
            'email': 'fjen@uwaterloo.ca',
            'phone': '(226) 972-0522',
            'address_id': 1
        }
        user = models.User(**user_kwargs)

        db.session.add(user)
        db.session.commit()

    @classmethod
    def workPlace(cls):
        pass

    @classmethod
    def workTask(cls):
        pass

    @classmethod
    def address(cls):
        """Generate addresses and insert them into database.
        """
        user_kwargs = {
            'suite_number': '302',
            'street_name': '321 Lester St.',
            'city': 'Waterloo',
            'province': 'ON',
            'postal_code': 'N2L 3W6',
            'country': 'Canada'
        }
        user_address = models.Address(**user_kwargs)

        school_kwargs = {
            'street_name': '200 University Ave W',
            'city': 'Waterloo',
            'province': 'ON',
            'postal_code': 'N2L 3G1',
            'country': 'Canada'
        }
        school_address = models.Address(**school_kwargs)

        db.session.add_all([user_address, school_address])
        db.session.commit()

    @classmethod
    def tag(cls):
        """Generate a list of tags and insert them into database.
        """
        for tag in ['Python', 'Ruby', 'Ruby on Rails', 'C', 'C++', 'Bash', 'Web'
                    'Database', 'Cloud', 'Perl', 'Tools', 'Server']:
            tag = models.Tag(name=tag)
            db.session.add(tag)
        db.session.commit()

    @classmethod
    def skill(cls):
        pass

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