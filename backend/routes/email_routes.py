from flask import Blueprint
from services.gmail_service import get_reply_emails

email_bp = Blueprint("email", __name__)

@email_bp.route("/emails")
def emails():

    messages = get_reply_emails()

    return {
        "Total Reply Mails": len(messages),
        "Messages": messages
    }