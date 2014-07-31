import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

ajen_webSite = Flask(__name__)

# TODO(AJen): import/create db
DEV_CONFIG = 'default-config.DevConfig'
CONFIG_FILE = os.environ.get('PRODUCTION_CONFIG', DEV_CONFIG)
ajen_webSite.config.from_object(CONFIG_FILE)
db = SQLAlchemy(ajen_webSite)

from app.views import views, error_views
from dbmodels import models
