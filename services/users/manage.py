from flask.cli import FlaskGroup
from project import app, db


# Configure the Flask CLI tool to run and manage the app from the command line.
cli = FlaskGroup(app)

@cli.command("recreate_db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    cli()