import pytest

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()