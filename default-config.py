from db import db_config

class DevConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = db_config.SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_MIGRATE_REPO = db_config.SQLALCHEMY_MIGRATE_REPO

class ProductionConfig(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = db_config.SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_MIGRATE_REPO = db_config.SQLALCHEMY_MIGRATE_REPO
