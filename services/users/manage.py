from flask.cli import FlaskGroup
from project import create_app, db
from project.api.models import User
import unittest


# Configure the Flask CLI tool to run and manage the app from the command line.
app =create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('test')
def test():
    """ Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@cli.command('seed_db')
def seed_db():
    """Seeds the database."""
    db.session.add(User(username='eray', email="me@gmail.com"))
    db.session.add(User(username='ozer', email="you@email.org"))
    db.session.commit()


if __name__ == '__main__':
    cli()