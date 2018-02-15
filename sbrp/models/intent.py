"""An intent is an inetion or pre-determined action."""
from sbrp.extensions import db

inent_reply_table = db.Table(
    'itent_replies', db.Model.metadata,
    db.Column('intents_id', db.Integer, db.ForeignKey('intents.id')),
    db.Column('replies_id', db.Integer, db.ForeignKey('replies.id'))
)


class Intent(db.Model):
    """An intent for action."""

    __tablename__ = 'intents'
    id = db.Column(db.Integer, primary_key=True)
    intent_key = db.Column(db.String(256), unique=True, nullable=False)
    active = db.Column(db.Boolean, default=True)

    replies = db.relationship(
        "Reply",
        secondary=inent_reply_table,
        backref="intents")
