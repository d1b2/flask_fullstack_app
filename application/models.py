from werkzeug.security import generate_password_hash, check_password_hash
from application import db,login_manager
from datetime import datetime,timedelta
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import jwt
from application.utils import read_json
from application.secret_filepaths import APP_INFO_SECRETS_PATH

app_info=read_json(APP_INFO_SECRETS_PATH)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(20), nullable=False)    
    username = db.Column(db.String(20), unique=True, nullable=False)
    dob=db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at=db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    last_modified_at=db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    num_modifications = db.Column(db.Integer, default=0)

    activity_id = db.relationship('Leisure_journal', backref='person')

    @property
    def password_hash(self):
        raise AttributeError('password is not a readable attribute!')
    
    @password_hash.setter
    def password_hash(self, user_entered_password):
        self.password_hash = generate_password_hash(user_entered_password)

    def verify_password(self, user_entered_password):
        return check_password_hash(self.password_hash, user_entered_password)
    
    def get_reset_paswd_token(self, expiration_time=datetime.utcnow()+timedelta(minutes=10)):
        payload={"user_id":self.id,"exp":expiration_time}
        token= jwt.encode(payload, app_info['secret_key'], algorithm="HS256")
        return token

    @staticmethod
    def verify_reset_token(token):        
        try:
            s = jwt.decode(token,app_info['secret_key'],algorithms=["HS256"])
            user_id = s['user_id']            
        except:
            return None
        return User.query.get(user_id)
    
    def __repr__(self):
        return f"User('{self.fullname}', '{self.username}', '{self.email}')"

class Leisure_journal(db.Model):
    leisure_id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String(50))
    description = db.Column(db.Text) 
    made_for=db.Column(db.String(10))
    duration=db.Column(db.Float,unique=False, nullable=False)
    made_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    # Foreign Key To Link Users (refer to primary key of the user)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))