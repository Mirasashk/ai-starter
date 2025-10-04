"""Pytest configuration and fixtures."""

import os
import sys

import pytest
from fastapi.testclient import TestClient

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from app import app


@pytest.fixture
def client() -> TestClient:
    """Create a test client for the FastAPI application."""
    return TestClient(app)


@pytest.fixture
def sample_data() -> dict:
    """Sample data for testing."""
    return {
        "text": "This is a sample text for testing",
        "label": "positive",
        "confidence": 0.95,
    }


@pytest.fixture
def sample_model_input() -> dict:
    """Sample model input for testing."""
    return {
        "features": [1.0, 2.0, 3.0, 4.0, 5.0],
        "metadata": {
            "timestamp": "2024-01-01T00:00:00Z",
            "source": "test",
        },
    }
