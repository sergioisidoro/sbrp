from flask_admin.contrib.sqla import ModelView

from holvibot.extensions import db
from holvibot.models.user import User

user_admin = ModelView(User, db.session)
