import pytest

from repository.database import create_tables, drop_tables


@pytest.fixture(scope="module")
def setup_database():
    create_tables()
    yield
    drop_tables()

# @pytest.fixture(scope="module")
# def movie(setup_database):
#     movie = insert_movie(Movie(title="the star", genre="drama", year=2012)).unwrap()
#     return movie
