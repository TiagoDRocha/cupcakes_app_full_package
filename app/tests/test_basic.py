import pytest
from app import create_app, db
def test_index_route():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        rv = client.get('/')
        assert rv.status_code == 200
