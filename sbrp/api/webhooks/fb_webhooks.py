
from flask import Blueprint, request, Response
from sbrp.models.bot import Bot


from fbmq import Page


# Setup Page

fb_webhook_blueprint = Blueprint('fb_webhook', __name__)

@fb_webhook_blueprint.route('/<str:bot_key>/webhook', methods=['POST']):
def incoming_fb_webhook(bot_key=None):
    """Handle a webhook from facebook."""

    bot = Bot.query.filter_by(bot_key=bot_key).get_or_404()
    fb_key = bot.fb_key

    if not fb_key:
        return Response(status='404')
    
    page = Page(fb_key)
    page.handle_webhook(request.get_data(as_text=True))
    
    return Response(status='200')



def message_handler(event):
    """:type event: fbmq.Event"""
    sender_id = event.sender_id
    message = event.message_text
            
    page.send(sender_id, "thank you! your message is '%s'" % message)

def after_send(payload, response):
    """:type event: fbmq.Payload"""
    print("complete")i


















