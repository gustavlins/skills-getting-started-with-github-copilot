from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

INITIAL_ACTIVITIES = deepcopy(activities)


@pytest.fixture()
def client():
    """Provide a test client with fresh in-memory activity state for each test."""
    # Arrange
    activities.clear()
    activities.update(deepcopy(INITIAL_ACTIVITIES))

    # Act
    with TestClient(app) as test_client:
        yield test_client

    # Assert
    # No explicit assertions needed for fixture cleanup.
