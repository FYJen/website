from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
address = Table('address', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('street_name', String(length=32)),
    Column('province', String(length=32)),
    Column('country', String(length=32)),
    Column('postal_code', String(length=32)),
    Column('active', Boolean, default=ColumnDefault(True)),
)

course = Table('course', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('initials', String(length=16)),
    Column('term', String(length=16)),
    Column('school_id', Integer),
)

project = Table('project', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=32)),
    Column('description', Text),
    Column('start_date', DateTime),
    Column('end_date', DateTime),
    Column('thumbnail', String(length=64)),
    Column('user_id', Integer),
)

school = Table('school', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=32)),
    Column('level', String(length=32)),
    Column('start_date', DateTime),
    Column('end_date', DateTime),
    Column('attending', Boolean, default=ColumnDefault(True)),
    Column('term', String(length=32)),
    Column('address_id', Integer),
)

schools = Table('schools', post_meta,
    Column('school_id', Integer),
    Column('user_id', Integer),
)

skill = Table('skill', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('description', Text),
    Column('selected', Boolean, default=ColumnDefault(True)),
    Column('user_id', Integer),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('first_name', String(length=32), nullable=False),
    Column('last_name', String(length=32), nullable=False),
    Column('email', String(length=64)),
    Column('phone', String(length=32)),
    Column('address_id', Integer),
)

work_place = Table('work_place', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=32)),
    Column('start_date', DateTime),
    Column('end_date', DateTime),
    Column('address_id', Integer),
    Column('user_id', Integer),
)

work_task = Table('work_task', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('description', Text),
    Column('workplace_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['address'].create()
    post_meta.tables['course'].create()
    post_meta.tables['project'].create()
    post_meta.tables['school'].create()
    post_meta.tables['schools'].create()
    post_meta.tables['skill'].create()
    post_meta.tables['user'].create()
    post_meta.tables['work_place'].create()
    post_meta.tables['work_task'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['address'].drop()
    post_meta.tables['course'].drop()
    post_meta.tables['project'].drop()
    post_meta.tables['school'].drop()
    post_meta.tables['schools'].drop()
    post_meta.tables['skill'].drop()
    post_meta.tables['user'].drop()
    post_meta.tables['work_place'].drop()
    post_meta.tables['work_task'].drop()
