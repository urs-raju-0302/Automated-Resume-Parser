from fastapi.testclient import TestClient
from backend.main import app
client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "healthy"

def test_invalid_file_type():
    r = client.post("/api/parse", files={"file": ("resume.txt", b"hello", "text/plain")})
    assert r.status_code == 400
