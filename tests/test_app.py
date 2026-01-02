from src.app import app as flask_app


def test_homepage_returns_hello():
    flask_app.testing = True
    client = flask_app.test_client()

    resp = client.get("/")
    assert resp.status_code == 200
    assert "Hello, World" in resp.get_data(as_text=True)
