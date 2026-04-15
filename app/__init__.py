from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # CONFIG CORRETA
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///finance.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # IMPORTS
    from app.models import User, Category, Transaction, Log
    from app.routes.users import users_bp
    from app.routes.categories import categories_bp
    from app.routes.transactions import transactions_bp

    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(categories_bp, url_prefix="/categories")
    app.register_blueprint(transactions_bp, url_prefix="/transactions")

    return app