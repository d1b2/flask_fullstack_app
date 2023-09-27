from flask import url_for, current_app
from flask_mail import Message
from application import mail
from application.utils import read_json
from application.secret_filepaths import MAIL_SECRETS_PATH

mail_keys=read_json(MAIL_SECRETS_PATH)


def send_reset_email(user):
    token = user.get_reset_paswd_token()
    msg = Message('Password Reset Request',
                  sender=mail_keys['MAIL_USERNAME_KEY'],
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:

{url_for('user.reset_token', token=token, _external=True)}

This token is valid for next 10 minutes only.


If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)
