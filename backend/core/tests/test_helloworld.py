from rest_framework import status
from django.conf import settings
import pytest

@pytest.fixture
def base_url():
    return f"/api/v{settings.VERSION}/"


class TestHelloWorld:
    def test_hello_world_success(self, api_client, base_url):
        response = api_client.get(f"{base_url}hello-world")
           
        assert response.status_code == status.HTTP_200_OK
        