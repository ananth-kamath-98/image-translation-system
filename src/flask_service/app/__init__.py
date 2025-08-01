from flask import Flask

from .config import Config
from .routes.dashboard import dashboard_blue_print
from .routes.login import main


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(main)
    app.register_blueprint(dashboard_blue_print)
    return app
