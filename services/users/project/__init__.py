# regarding werkzeug import->https://stackoverflow.com/a/60157748 # noqa: E402
import werkzeug  # noqa: E402
werkzeug.cached_property = werkzeug.utils.cached_property  # noqa: E402
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension


db = SQLAlchemy()
toolbar = DebugToolbarExtension()


# adding the Application Factory pattern
def create_app(script_info=None):
    app = Flask(__name__)
    app.config.from_object(os.getenv('APP_SETTINGS'))

    # set up extensions
    db.init_app(app)
    toolbar.init_app(app)

    # register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    # shell context for flask cli. Now we can work with the application context
    # and the database without having to import them directly into the shell
    app.shell_context_processor({'app': app, 'db': db})
    return app
