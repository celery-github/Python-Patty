from app import app

def test_homepage_returns_hello():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Hello, World" in resp.data
