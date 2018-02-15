from flask_admin.contrib.sqla import ModelView

from sbrp.extensions import db
from sbrp.models.user import User

user_admin = ModelView(User, db.session)
