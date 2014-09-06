from app import ajen_webSite
from app.config import default_config as setting
from flask import render_template

@ajen_webSite.errorhandler(404)
def page_not_found(error):
    return render_template('/error/404.html', headers=setting.BASE_PAGE), 404

@ajen_webSite.errorhandler(500)
def internal_server_error(error):
    return render_template('/error/500.html', headers=setting.BASE_PAGE), 500
