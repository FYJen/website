from app import db

# Many-tomany table for Users and Schools.
schools = db.Table('schools',
    db.Column('school_id'), db.Integer, db.ForeignKey('school.id'),
    db.Column('user_id'), db.Integer, db.ForeignKey('user.id'),
)

class User(db.Model):
    """
    A User is a single entity containing basic data about that person.

    Users are many-to-many with Schools.
    Users are many-to-one with Addresses.
    Users are one-to-many with WorkPlaces.
    Users are one-to-many with Skills.
    Users are one-to-many with Projects.
    """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(64), index=True, unique=True)
    phone = db.Column(db.String(32))
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))

    work_places = db.relationship('WorkPlace', backref='employee', lazy='dynamic')
    skills = db.relationship('Skill', backref='possessor', lazy='dynamic')
    projects = db.relationship('Project', backref='owner', lazy='dynamic')
    schools = db.relationship('School', secondary=schools,
                              backref=db.backref('students', lazy='dynamic'))

    def __repr__(self):
        return '<User %r>' % (self.email)

class WorkPlace(db.Model):
    """
    A WorkPlace is a single work location where I have worked. WorkPlace will
    capture the name of the company, start and end day, location and a list of
    tasks involved.

    WorkPlaces are one-to-many with WorkTasks.
    WorkPlaces are one-to-one with Addresses.
    WorkPlaces are many-to-one with Users.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    work_tasks = db.relationship('WorkTask', backref='workplace', lazy='dynamic')

    def __repr__(self):
        return '<WorkPlace %r>' % (self.name)

class WorkTask(db.Model):
    """
    A WorkTask is a single task that has been achieved at a WorkPlace.

    WorkTasks are many-to-one with WorkPlaces.
    """
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    workplace_id = db.Column(db.Integer, db.ForeignKey('workplace.id'))

    def __repr__(self):
        return '<WorkTask %r>' % (self.id)

class Address(db.Model):
    """
    An Address is a location.

    Addresses are one-to-many with User.
    Addresses are one-to-one with WorkPlace.
    Addresses are one-to-one with Schools.
    """
    id = db.Column(db.Integer, primary_key=True)
    street_name = db.Column(db.String(32))
    province = db.Column(db.String(32))
    country = db.Column(db.String(32))
    postal_code = db.Column(db.String(32))

    user_addr = db.relationship('User', backref='address')
    school_addr = db.relationship('School', backref='address', uselist=False)
    workplace_addr = db.relationship('WorkPlace', backref='address',
                                     uselist=False)

    def __repr__(self):
        return '<Address %r>' % (self.street_name)

class Skill(db.Model):
    """
    A Skill is a single technique that a person possesses.

    Skills are many-to-one with Users.
    """
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    active = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Skill %r>' % (self.id)

class School(db.Model):
    """
    A School is a single institution.

    Schools are many-to-many with Users.
    Schools are one-to-one with Addresses.
    Schools are one-to-many with Courses.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True, unique=True)
    level = db.Column(db.String(32))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))

    courses = db.relationship('Course', backref='school', lazy='dynamic')

    def __repr__(self):
        return '<School %r>' % (self.name)

class Course(db.Model):
    """
    A Course is a single course that a shcool offers.

    Courses are many-to-one with Schools.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    initials = db.Column(db.String(16))
    term = db.Column(db.String(16))
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'))

class Project(db.Model):
    """
    A Project is a single personal work.

    Projects are many-to-one with Users.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    description = db.Column(db.Text)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    thumbnail = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Project %r>' % (self.name)
