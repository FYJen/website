import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

ajen_webSite = Flask(__name__)
ajen_api = Flask('api')

# Website configuration.
WEB_DEV_CONFIG = 'default-config.WebDevConfig'
WEB_CONFIG_FILE = os.environ.get('WEB_PRODUCTION_CONFIG', WEB_DEV_CONFIG)
ajen_webSite.config.from_object(WEB_CONFIG_FILE)

# API configuration
API_DEV_CONFIG = 'default-config.APIDevConfig'
API_CONFIG_FILE = os.environ.get('API_PRODUCTION_CONFIG', API_DEV_CONFIG)
ajen_api.config.from_object(API_CONFIG_FILE)

# DB configuration.
db = SQLAlchemy(ajen_api)

from app.views import content_views, api_views, error_views
from dbmodels import models
