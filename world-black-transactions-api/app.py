from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    CORS(app)

    if not app.debug:
        import logging
        from logging.handlers import RotatingFileHandler
        file_handler = RotatingFileHandler('error.log', maxBytes=10240, backupCount=10)
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

    with app.app_context():
        from app.routes import main_routes
        app.register_blueprint(main_routes)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=app.config['DEBUG'], port=8080)
