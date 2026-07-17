from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.main import create_app


def test_create_app_returns_fastapi_instance() -> None:
    assert isinstance(create_app(), FastAPI)


def test_healthz_returns_200() -> None:
    client = TestClient(create_app())
    response = client.get("/healthz")
    assert response.status_code == 200


def test_healthz_body() -> None:
    client = TestClient(create_app())
    response = client.get("/healthz")
    assert response.json() == {"status": "ok"}


def test_healthz_content_type() -> None:
    client = TestClient(create_app())
    response = client.get("/healthz")
    assert response.headers["content-type"] == "application/json"


def test_unknown_route_returns_404() -> None:
    client = TestClient(create_app())
    response = client.get("/not-a-real-path")
    assert response.status_code == 404
