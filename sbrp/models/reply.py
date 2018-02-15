"""A Reply is a premade response to a certain action."""
from sbrp.extensions import db


class Reply(db.Model):
    """A premade response."""

    __tablename__ = 'replies'
    id = db.Column(db.Integer, primary_key=True)
    message_key = db.Column(db.String(256), unique=True, nullable=False)
    message = db.Column(db.Text())

    active = db.Column(db.Boolean, default=True)
