from db import db_config

class BasicConfig(object):
    SQLALCHEMY_DATABASE_URI = db_config.SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_MIGRATE_REPO = db_config.SQLALCHEMY_MIGRATE_REPO

class WebDevConfig(BasicConfig):
    DEBUG = True
    SERVER_NAME = 'localhost:8080'

class WebProductionConfig(BasicConfig):
    DEBUG = False
    SERVER_NAME = 'www.arthur-jen.com'

class APIDevConfig(BasicConfig):
    DEBUG = True
    SERVER_NAME = 'localhost:5050'

class APIProductionConfig(BasicConfig):
    DEBUG = False
    SERVER_NAME = 'www.arthur-jen.com'
