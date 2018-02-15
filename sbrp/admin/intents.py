from flask_admin.contrib.sqla import ModelView

from sbrp.extensions import db
from sbrp.models.intent import Intent
from sbrp.models.reply import Reply
from sbrp.models.bot import Bot

intent_admin = ModelView(Intent, db.session)
reply_admin = ModelView(Reply, db.session)
bot_admin = ModelView(Bot, db.session)
