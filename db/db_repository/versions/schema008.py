from app import db

# Many-to-many table for Users and Schools.
users_schools = db.Table('users_schools',
    db.Column('school_id', db.Integer, db.ForeignKey('school.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

class User(db.Model):
    """
    A User is a single entity containing basic information about that person.

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
    alt_email = db.Column(db.String(64), index=True, unique=True)
    phone = db.Column(db.String(32))
    github = db.Column(db.String(64), unique=True)
    linkedin = db.Column(db.String(64), unique=True)
    skype = db.Column(db.String(64), unique=True)
    intro = db.Column(db.Text)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))

    workPlaces = db.relationship('WorkPlace', backref='employee', lazy='dynamic')
    skills = db.relationship('Skill', backref='possessor', lazy='dynamic')
    projects = db.relationship('Project', backref='owner', lazy='dynamic')
    schools = db.relationship('School', secondary=users_schools,
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
    __tablename__ = 'work_place'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    initial = db.Column(db.String(32))
    position_title = db.Column(db.String(32), nullable=False)
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
    __tablename__ = 'work_task'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    workplace_id = db.Column(db.Integer, db.ForeignKey('work_place.id'))

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
    apt_number = db.Column(db.String(32))
    suite_number = db.Column(db.String(32))
    floor = db.Column(db.String(32))
    street_name = db.Column(db.String(32))
    city = db.Column(db.String(32))
    province_state = db.Column(db.String(32))
    country = db.Column(db.String(32))
    postalcode_zip = db.Column(db.String(32))
    active = db.Column(db.Boolean, default=True)

    users = db.relationship('User', backref='address', lazy='dynamic')
    school = db.relationship('School', backref='address', uselist=False)
    workPlace = db.relationship('WorkPlace', backref='address',
                                 uselist=False)

    def __repr__(self):
        return '<Address %r>' % (self.street_name)

class Tag(db.Model):
    """A Tag is a type of skill.

    Tags are one-to-many with SKills.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)

    skills = db.relationship('Skill', backref='tag', lazy='dynamic')

class Skill(db.Model):
    """
    A Skill is a single technique that a person possesses.

    Skills are many-to-one with Users.
    Skills are many-to-one with Tags.
    """
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    selected = db.Column(db.Boolean, default=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
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
    degree = db.Column(db.String(64))
    major = db.Column(db.String(64))
    minor = db.Column(db.String(64))
    joint = db.Column(db.String(64))
    level = db.Column(db.String(32))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    attending = db.Column(db.Boolean, default=True)
    term = db.Column(db.String(32))
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))

    courses = db.relationship('Course', backref='school', lazy='dynamic')

    def __repr__(self):
        return '<School %r>' % (self.name)

class Course(db.Model):
    """
    A Course is a single course that a school offers.

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
    Projects are one-to-many with ProjectTask
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    thumbnail = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    project_tasks = db.relationship('ProjectTask', backref='project',
                                    lazy='dynamic')

    def __repr__(self):
        return '<Project %r>' % (self.name)

class ProjectTask(db.Model):
    """
    A ProjectTask is single description for a Project.

    ProjectTasks are many-to-one with Projects.
    """
    __tablename__ = 'project_task'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

    def __repr__(self):
        return '<ProjectTask %r>' % (self.id)
