import click
from flask.cli import FlaskGroup

from sbrp.app import create_app


def create_sbrp(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_sbrp)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Init application, create database tables
    and create a new user named admin with password admin
    """
    from sbrp.extensions import db
    from sbrp.models import User
    click.echo("create database")
    db.create_all()
    click.echo("done")

    click.echo("create user")
    user = User(
        username='admin',
        email='admin@mail.com',
        password='admin',
        active=True
    )
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")


if __name__ == "__main__":
    cli()
