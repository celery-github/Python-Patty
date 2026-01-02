import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app import app as flask_app  # noqa: E402


def test_homepage_returns_hello():
    flask_app.testing = True
    client = flask_app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert "Hello, World" in resp.get_data(as_text=True)
