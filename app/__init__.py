from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)

    from .routes import words_bp
    app.register_blueprint(words_bp)

    return app
