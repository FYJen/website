from app import db

class User(db.Model):
    """
    Users are many-to-one with Addresses.
    """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(64), index=True, unique=True)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))

    def __repr__(self):
        return '<User %r>' % (self.email)

class WorkPlace(db.Model):
    """
    WorkPlaces are one-to-many with WorkTasks.
    WorkPlaces are one-to-one with Addresses.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    work_tasks = db.relationship('WorkTask', backref='workplace', lazy='dynamic')
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))

    def __repr__(self):
        return '<WorkPlace %r>' % (self.name)

class WorkTask(db.Model):
    """
    WorkTasks are many-to-one with WorkPlaces.
    """
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    workplace_id = db.Column(db.Integer, db.ForeignKey('workplace.id'))

    def __repr__(self):
        return '<WorkTask %r>' % (self.id)

class Address(db.Model):
    """
    Addresses are one-to-many with User.
    Addresses are one-to-one with WorkPlace.
    """
    id = db.Column(db.Integer, primary_key=True)
    street_name = db.Column(db.String(32))
    province = db.Column(db.String(32))
    country = db.Column(db.String(32))
    postal_code = db.Column(db.String(32))
    user_addr = db.relationship('User', backref='address')
    workplace_addr = db.relationship('WorkPlace', backref='address')

    def __repr__(self):
        return '<Address %r>' % (self.street_name)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)

    def __repr__(self):
        return '<Skill %r>' % (self.id)

class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    level = db.Column(db.String(32))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)

    def __repr__(self):
        return '<School %r>' % (self.name)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    description = db.Column(db.Text)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)

    def __repr__(self):
        return '<Project %r>' % (self.name)
