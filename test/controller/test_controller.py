import pytest
from flask import Flask

from repository.database import create_tables, drop_tables
from service.seed import seed


@pytest.fixture
def app():
    app = Flask(__name__)
    # app.register_blueprint(user_blueprint, url_prefix="/api/user")
    # app.register_blueprint(store_blueprint, url_prefix="/api/store")
    # app.register_blueprint(movie_blueprint, url_prefix="/api/movie")
    # app.register_blueprint(subscription_blueprint, url_prefix="/api/subscription")
    # app.register_blueprint(rental_blueprint, url_prefix="/api/rental")
    return app

@pytest.fixture
def client(app):
    create_tables()
    seed()
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client
    drop_tables()