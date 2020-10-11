import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property #https://stackoverflow.com/a/60157748
from flask import Flask, jsonify
import os
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

#adding the Application Factory pattern
def create_app(script_info=None):
    app = Flask(__name__)
    app.config.from_object(os.getenv('APP_SETTINGS'))

    # set up extensions
    db.init_app(app)

    # register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)


    # shell context for flask cli. Now we can work with the application context 
    # and the database without having to import them directly into the shell
    app.shell_context_processor({'app': app, 'db': db})
    return app