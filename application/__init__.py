from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from application.config import Config
from flask_mail import Mail

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'user.login'
login_manager.login_message_category = 'info'
mail=Mail()


#app config settings
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from application.user.routes import user
    from application.main.routes import main    
    app.register_blueprint(user)
    app.register_blueprint(main)

    return app