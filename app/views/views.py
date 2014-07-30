from app import ajen_webSite
from app.config import default_config as setting
from flask import render_template

@ajen_webSite.route('/', methods=['GET'])
@ajen_webSite.route('/about/', methods=['GET'])
def about():
    return render_template('about.html', headers=setting.BASE_PAGE)

@ajen_webSite.route('/resume/', methods=['GET'])
def resume():
    return render_template('resume.html', headers=setting.BASE_PAGE)

@ajen_webSite.route('/projects/', methods=['GET'])
def projects():
    return render_template('projects.html', headers=setting.BASE_PAGE)

@ajen_webSite.route('/contact/', methods=['GET'])
def contact():
    return render_template('contact.html', headers=setting.BASE_PAGE)
