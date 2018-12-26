# -*- coding: utf-8 -*-
import os
"""The app module, containing the app factory function."""
from flask import Flask, render_template

# from  import commands, public, user
from app.index.views import index_blueprint
from flask_migrate import MigrateCommand
from extensions import (
    bcrypt, 
    db, 
    migrate,
    ma,
    redis_store,
)
import logging.config
# from settings import base_settings

SETTINGS_FILE = os.environ.get("SETTINGS_FILE", "settings.dev_settings")


def create_app(config_object='settings.base_settings'):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.config.from_object(SETTINGS_FILE)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    # register_shellcontext(app)
    # register_commands(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    bcrypt.init_app(app)
    # cache.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    redis_store.init_app(app)
    logging.config.dictConfig(app.config["LOGGING"])
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    # app.register_blueprint(public.views.blueprint)
    app.register_blueprint(index_blueprint, url_prefix="/index")
    return None


def register_errorhandlers(app):
    """Register error handlers."""
    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template('{0}.html'.format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None


def register_shellcontext(app):
    """Register shell context objects."""
    def shell_context():
        """Shell context objects."""
        return {
            'db': db,
            'User': user.models.User}

    app.shell_context_processor(shell_context)


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.test)
    app.cli.add_command(commands.lint)
    app.cli.add_command(commands.clean)
    app.cli.add_command(commands.urls)
