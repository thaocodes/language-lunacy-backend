from flask import Flask
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app, origins=['http://localhost:3000'])

    from .routes import words_bp
    app.register_blueprint(words_bp)

    return app
