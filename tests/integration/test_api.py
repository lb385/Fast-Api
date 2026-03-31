from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_add_endpoint() -> None:
    response = client.post("/add", json={"a": 4, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 7}


def test_subtract_endpoint() -> None:
    response = client.post("/subtract", json={"a": 10, "b": 6})
    assert response.status_code == 200
    assert response.json() == {"result": 4}


def test_multiply_endpoint() -> None:
    response = client.post("/multiply", json={"a": 5, "b": 8})
    assert response.status_code == 200
    assert response.json() == {"result": 40}


def test_divide_endpoint() -> None:
    response = client.post("/divide", json={"a": 20, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_divide_by_zero_returns_400() -> None:
    response = client.post("/divide", json={"a": 20, "b": 0})
    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot divide by zero"}
