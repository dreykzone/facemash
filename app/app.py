from flask import Flask
from app.routes.routes import routes
from app.ext.configuration import Config
from app.ext.database import db

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(routes)
    
    return app