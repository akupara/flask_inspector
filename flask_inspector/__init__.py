# coding: utf-8
from flask import render_template, Blueprint
import os
import warnings

from .versions import get_git_changeset
from .auth import BaseAuth


baseauth = BaseAuth()


class InspectorView(object):
    def __init__(self, inspector=None):
        self.inspector = inspector
        self.app = inspector.app

    @baseauth.requires_auth
    def __call__(self):
        inspector = self.inspector
        git_log = inspector.git_log or ''

        env = os.environ.get('MODE', '')
        configs = {
            'env': env
        }
        app_config = self.app.config
        for config_key in app_config:
            if config_key in inspector.ignore_configs:
                continue
            val = app_config[config_key]
            if not isinstance(val, (str, unicode, int, long, bool)):
                continue
            configs[config_key] = val

        params = {
            'git_log': git_log.replace('\n', '').decode('utf-8'),
            'configs': configs
        }

        return render_template('inspector.html', **params)

    __name__ = 'inspector_view'


class Inspector(object):
    def __init__(self,
                 app=None,
                 base_path=None,
                 url_prefix=None,
                 endpoint=None,
                 template=None,
                 ignore_configs=None,
                 username=None,
                 password=None):
        if not username or not password:
            warnings.warn('username or password must be set')
        else:
            baseauth._check_auth = self.check_auth
        self.username = username
        self.password = password
        self.app = app
        self.template = template or 'inspector.html'
        self.base_path = base_path
        self.git_log = ''
        self.url_prefix = url_prefix or '/inspector'
        self.endpoint = endpoint
        self.blueprint = None
        self.ignore_configs = ignore_configs or ('SECRET_KEY', )
        if app is not None:
            self.init_app(app)

    def check_auth(self, username, password):
        return self.username == username and self.password == password

    def init_app(self, app):
        self.app = app
        self.git_log = get_git_changeset(self.base_path)

        self.blueprint = Blueprint('inspector',
                                   __name__,
                                   url_prefix=self.url_prefix,
                                   template_folder='templates',
                                   static_folder='static'
                                   )
        view_func = InspectorView(self)
        self.blueprint.add_url_rule('/', view_func=view_func)

        app.register_blueprint(self.blueprint)
