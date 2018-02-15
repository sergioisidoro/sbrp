from flask import Flask

from sbrp import auth, api, admin
from sbrp.extensions import db, jwt, migrate, admin_app


def create_app(config=None, testing=False, cli=False):
    """Application factory, used to create application
    """
    app = Flask('sbrp')

    configure_app(app, testing)
    configure_extensions(app, cli)
    configure_admin(admin_app)
    register_blueprints(app)

    return app


def configure_app(app, testing=False):
    """set configuration for application
    """
    # default configuration
    app.config.from_object('sbrp.config')

    if testing is True:
        # override with testing config
        app.config.from_object('sbrp.configtest')
    else:
        # override with env variable, fail silently if not set
        app.config.from_envvar("SBRP_CONFIG", silent=True)


def configure_extensions(app, cli):
    """configure flask extensions
    """
    db.init_app(app)
    jwt.init_app(app)
    admin_app.init_app(app)
    if cli is True:
        migrate.init_app(app, db)


def register_blueprints(app):
    """register all blueprints for application
    """
    app.register_blueprint(auth.views.blueprint)
    app.register_blueprint(api.views.blueprint)


def configure_admin(admin_app):
    """Register blueprints of admin views."""

    admin_app.add_view(admin.user_admin)
    admin_app.add_view(admin.intent_admin)
    admin_app.add_view(admin.reply_admin)
    admin_app.add_view(admin.bot_admin)
