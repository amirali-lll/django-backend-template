from rest_framework.test import APIClient
from pytest import fixture

@fixture
def api_client():
    return APIClient()