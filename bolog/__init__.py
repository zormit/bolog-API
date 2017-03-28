from bolog.blueprints import books
from bolog.api_components import ApiFlask, ApiException


def create_app(config=None):
    app = ApiFlask(__name__)
    app.config.update(config or {})
    app.register_blueprint(books)
    register_error_handlers(app)
    return app


def register_error_handlers(app):
    app.register_error_handler(
        ApiException, lambda err: err.to_result())
