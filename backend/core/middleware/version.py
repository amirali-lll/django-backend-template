from django.utils.deprecation import MiddlewareMixin
from django.conf import settings


class VersionMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-API-Version'] = settings.API_VERSION
        return response