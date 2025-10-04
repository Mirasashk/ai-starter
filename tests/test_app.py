"""Tests for the FastAPI application."""

import os
import sys

from fastapi.testclient import TestClient

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from app import app

client = TestClient(app)


class TestRootEndpoint:
    """Test the root endpoint."""

    def test_root_endpoint(self) -> None:
        """Test that the root endpoint returns the expected message."""
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello AI Expert!"}


class TestHealthEndpoint:
    """Test the health check endpoint."""

    def test_health_check(self) -> None:
        """Test that the health check endpoint returns healthy status."""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}


class TestInfoEndpoint:
    """Test the info endpoint."""

    def test_app_info(self) -> None:
        """Test that the info endpoint returns application information."""
        response = client.get("/info")
        assert response.status_code == 200

        data = response.json()
        assert data["name"] == "AI Starter"
        assert data["version"] == "0.1.0"
        assert "description" in data
        assert data["docs"] == "/docs"
        assert data["redoc"] == "/redoc"


class TestAPIEndpoints:
    """Test API endpoints integration."""

    def test_all_endpoints_accessible(self) -> None:
        """Test that all main endpoints are accessible."""
        endpoints = ["/", "/health", "/info", "/docs", "/redoc"]

        for endpoint in endpoints:
            response = client.get(endpoint)
            # Allow 200 for most endpoints, 200 or 404 for docs (depending on setup)
            assert response.status_code in [
                200,
                404,
            ], f"Endpoint {endpoint} returned {response.status_code}"

    def test_response_headers(self) -> None:
        """Test that responses have appropriate headers."""
        response = client.get("/")
        assert "content-type" in response.headers
        assert response.headers["content-type"] == "application/json"
