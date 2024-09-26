import pytest

from repository.database import create_tables, drop_tables
from repository.target_repository import find_targets, find_target_by_id
from service.seed import seed


@pytest.fixture(scope="module")
def setup_database():
    seed()
    yield
    drop_tables()

def test_find_targets(setup_database):
    targets = find_targets()
    assert targets
    assert len(targets) > 0

def test_find_target_by_id(setup_database):
    target = find_target_by_id(1)
    assert target
    assert target.value_or(None).target_id == 1

