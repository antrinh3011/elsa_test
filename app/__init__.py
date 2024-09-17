from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO

db = SQLAlchemy()
migrate = Migrate()
socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app)

    from app.routes import main_bp
    app.register_blueprint(main_bp)

    from app.sockets import setup_socketio
    setup_socketio(app)

    return app
