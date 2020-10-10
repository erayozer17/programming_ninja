from flask.cli import FlaskGroup
from project import app


# Configure the Flask CLI tool to run and manage the app from the command line.
cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()