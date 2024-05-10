
from rest_framework.response import Response
from typing import Any
from core import messages


class CustomResponseMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # if response is file return it 
        if isinstance(response, (bytes, bytearray)):
            return response
        if isinstance(response, Response) and response.accepted_renderer.format in ['json','api']:
            # set message using response status
            if response.status_code < 400:
                message = messages.SUCCESS
            elif response.status_code == 404:
                message = messages.NOT_FOUND
            elif response.status_code == 403:
                message = messages.FORBIDDEN
            elif response.status_code == 401:
                message = messages.UNAUTHORIZED
            else:
                message = messages.ERROR
            # check if message is set in response data or not
            if response.data != None and 'message' in response.data:
                # pop the message from data and set it as message
                message = response.data.pop('message')
                # message = response.data['message']
            data = {
                'status':response.status_code,
                'is_success':response.status_code < 400,
                'message':message,
                'data':response.data,
                'errors':response.data if response.status_code >= 400 else None
            }
            response.data = data
            response._is_rendered = False 
            response.render()
        return response