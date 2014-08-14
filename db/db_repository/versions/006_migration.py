"""Migrations:
   - Rename workplace table to work_place table.
   - Rename schools table to users_schools table.
   - Add new project_task table.
   - Remove description column from project table.
   - Add new columns, degree, joint, major, minor to school table.
   - Add new columns, github and linkedin to user table. 
"""

from sqlalchemy import *
from migrate import *
from migrate.changeset import schema

pre_meta = MetaData()
post_meta = MetaData()

schools = Table('schools', pre_meta,
    Column('school_id', INTEGER),
    Column('user_id', INTEGER),
)

workplace = Table('workplace', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=32)),
    Column('start_date', DATETIME),
    Column('end_date', DATETIME),
    Column('address_id', INTEGER),
    Column('user_id', INTEGER),
    Column('initial', VARCHAR(length=32)),
    Column('position_title', VARCHAR(length=32)),
)

project_task = Table('project_task', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('description', Text),
    Column('project_id', Integer),
)

users_schools = Table('users_schools', post_meta,
    Column('school_id', Integer, primary_key=True, nullable=False),
    Column('user_id', Integer, primary_key=True, nullable=False),
)

work_place = Table('work_place', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=32)),
    Column('initial', String(length=32)),
    Column('position_title', String(length=32)),
    Column('start_date', DateTime),
    Column('end_date', DateTime),
    Column('address_id', Integer),
    Column('user_id', Integer),
)

project = Table('project', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=32)),
    Column('description', TEXT),
    Column('start_date', DATETIME),
    Column('end_date', DATETIME),
    Column('thumbnail', VARCHAR(length=64)),
    Column('user_id', INTEGER),
)

school = Table('school', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=32)),
    Column('degree', String(length=64)),
    Column('major', String(length=64)),
    Column('minor', String(length=64)),
    Column('joint', String(length=64)),
    Column('level', String(length=32)),
    Column('start_date', DateTime),
    Column('end_date', DateTime),
    Column('attending', Boolean, default=ColumnDefault(True)),
    Column('term', String(length=32)),
    Column('address_id', Integer),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('first_name', String(length=32), nullable=False),
    Column('last_name', String(length=32), nullable=False),
    Column('email', String(length=64)),
    Column('phone', String(length=32)),
    Column('github', String(length=64)),
    Column('linkedin', String(length=64)),
    Column('address_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['schools'].rename('users_schools')
    pre_meta.tables['workplace'].rename('work_place')
    post_meta.tables['project_task'].create()
    pre_meta.tables['project'].columns['description'].drop()
    post_meta.tables['school'].columns['degree'].create()
    post_meta.tables['school'].columns['joint'].create()
    post_meta.tables['school'].columns['major'].create()
    post_meta.tables['school'].columns['minor'].create()
    post_meta.tables['user'].columns['github'].create()
    post_meta.tables['user'].columns['linkedin'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['users_schools'].rename('schools')
    post_meta.tables['work_place'].rename('workplace')
    post_meta.tables['project_task'].drop()
    pre_meta.tables['project'].columns['description'].create()
    post_meta.tables['school'].columns['degree'].drop()
    post_meta.tables['school'].columns['joint'].drop()
    post_meta.tables['school'].columns['major'].drop()
    post_meta.tables['school'].columns['minor'].drop()
    post_meta.tables['user'].columns['github'].drop()
    post_meta.tables['user'].columns['linkedin'].drop()
