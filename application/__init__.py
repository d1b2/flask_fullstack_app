from flask import Flask
from application.config import Config


#app config settings
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from application.user.routes import user
    from application.main.routes import main    
    app.register_blueprint(user)
    app.register_blueprint(main)

    return app