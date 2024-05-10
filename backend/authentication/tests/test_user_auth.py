from rest_framework import status
from django.conf import settings
from django.contrib.auth import get_user_model
from model_bakery import baker
import pytest

User = get_user_model()



@pytest.fixture
def base_auth_url():
    return f"/api/v{settings.VERSION}/auth/"


@pytest.mark.django_db
class TestUserLogin:
    def test_login_with_valid_username_and_password(self, api_client, base_auth_url):
        user = baker.make(User)
        user.set_password("password")
        user.save()
        data = {
            "username": user.username,
            "password": "password",
        }

        response = api_client.post(f"{base_auth_url}login/", data=data)
        
        assert response.status_code == status.HTTP_200_OK
        assert "tokens" in response.data

    def test_login_with_valid_email_and_password(self, api_client, base_auth_url):
        user = baker.make(User)
        user.set_password("password")
        user.save()
        data = {
            "email": user.email,
            "password": "password",
        }

        response = api_client.post(f"{base_auth_url}login/", data=data)
        
        assert response.status_code == status.HTTP_200_OK
        assert "tokens" in response.data

    def test_login_with_invalid_username_get400(self, api_client, base_auth_url):
        user = baker.make(User)
        user.set_password("password")
        user.save()
        data = {
            "username": "invalid_username",
            "password": "password",
        }

        response = api_client.post(f"{base_auth_url}login/", data=data)
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "non_field_errors" in response.data

    def test_login_with_invalid_email_get400(self, api_client, base_auth_url):
        user = baker.make(User)
        user.set_password("password")
        user.save()
        data = {
            "email": "invalid_email@example.com",
            "password": "password",
        }

        response = api_client.post(f"{base_auth_url}login/", data=data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "non_field_errors" in response.data


    def test_if_send_both_username_and_email_get400(self, api_client, base_auth_url):
        user = baker.make(User)
        user.set_password("password")
        user.save()
        data = {
            "username": user.username,
            "email": user.email,
            "password": "password",
        }

        response = api_client.post(f"{base_auth_url}login/", data=data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "non_field_errors" in response.data

    def test_login_with_invalid_password_get400(self, api_client, base_auth_url):
        user = baker.make(User)
        user.set_password("password")
        user.save()
        data = {
            "username": user.username,
            "password": "invalid_password",
        }

        response = api_client.post(f"{base_auth_url}login/", data=data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "non_field_errors" in response.data

    def test_login_with_no_username_or_email_get400(self, api_client, base_auth_url):
        user = baker.make(User)
        user.set_password("password")
        user.save()
        data = {
            "password": "password",
        }

        response = api_client.post(f"{base_auth_url}login/", data=data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "non_field_errors" in response.data
    

    def test_login_with_no_password_get400(self, api_client, base_auth_url):
        user = baker.make(User)
        user.set_password("password")
        user.save()
        data = {
            "username": user.username,
        }

        response = api_client.post(f"{base_auth_url}login/", data=data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "password" in response.data

    def test_login_with_no_username_email_and_password_get400(self, api_client, base_auth_url):
        user = baker.make(User)
        user.set_password("password")
        user.save()
        data = {}

        response = api_client.post(f"{base_auth_url}login/", data=data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "password" in response.data
