from flask import Flask
from app.routes.routes import routes
from app.ext.configuration import Config
from app.ext.database import db, migrate
from app.models.person import Persons
from app.seed import seed_database

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(routes)

    @app.cli.command("seed")
    def seed_command():
        """Popula o banco com dados de exemplo quando ele estiver vazio."""
        seed_database()
        print("Seed concluído.")
    
    return app