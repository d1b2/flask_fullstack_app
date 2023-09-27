from application.utils import read_json
from application.secret_filepaths import *

app_info=read_json(APP_INFO_SECRETS_PATH)
db_keys=read_json(DB_SECRETS_PATH)
mail_keys=read_json(MAIL_SECRETS_PATH)

class Config:
    SECRET_KEY = app_info['secret_key']
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{db_keys['new_user_key']}:{db_keys['new_user_pswd_key']}@localhost/{db_keys['new_db']}"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = mail_keys['MAIL_USERNAME_KEY']
    MAIL_PASSWORD = mail_keys['MAIL_PASSWORD_KEY']
    