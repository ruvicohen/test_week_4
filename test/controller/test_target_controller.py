import pytest
from flask import Flask

from controller.target_controller import target_blueprint
from repository.database import create_tables, drop_tables
from repository.tables_native_sql_repository import insert_from_mission_to_target
from service.seed import seed


@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(target_blueprint, url_prefix="/api/target")
    return app

@pytest.fixture
def client(app):
    create_tables()
    seed()
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client
    drop_tables()

def test_find_targets(client):
    response = client.get('/api/target/')
    assert response.status_code == 200

def test_find_target_by_id(client):
    response = client.get('/api/target/1')
    assert response.status_code == 200
    assert response.json["body"]["target"]["target_id"] == 1
