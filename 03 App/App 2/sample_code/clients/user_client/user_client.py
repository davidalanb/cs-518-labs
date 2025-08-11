# from fastapi.exceptions import RequestValidationError
import requests as rq
import json

try:
    from api_client import APIClient
except ModuleNotFoundError:
    from clients.user_client.api_client import APIClient

class UserClient(APIClient):

    def __init__(self,url):
        super().__init__(url)

    # You can add other methods that are unique to User here