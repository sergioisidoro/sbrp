"""A bot is a group of actions intents specific to a certain task."""

from sbrp.extensions import db


class Bot(db.Model):
    """A single bot, with a name and a language."""

    __tablename__ = 'bots'
    id = db.Column(db.Integer, primary_key=True)
    bot_key = db.Column(db.String(256), unique=True, nullable=False)
    bot_name = db.Column(db.String(256), unique=True, nullable=False)

    # TODO: This is an mvp. 
    # Here  should be the key to a secure key-value store in the future!
    fb_key = db.Column(db.String(512), unique=True, nullable=False)

    language = db.Column(db.String(3), nullable=False)

    active = db.Column(db.Boolean, default=True)
