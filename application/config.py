import json


with open('secrets/secrets.json') as secret:
        app_info=json.load(secret)


with open('secrets/db_secrets.json') as secret:
        db_keys=json.load(secret)

class Config:
    SECRET_KEY = app_info['secret_key']
    #SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{db_keys['new_user_key']}:{db_keys['new_user_pswd_key']}@localhost/{db_keys['new_db']}"
    