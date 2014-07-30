from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

ajen_webSite = Flask(__name__)

# TODO(AJen): import/create db

from app.views import views, error_views
