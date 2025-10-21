class APIClientError(Exception):
    def __init__(self, response):
        self.status_code = response.status_code
        self.detail = response.text

class AuthenticationError(APIClientError):
    '''raise this when there is a 401'''

class ResourceNotFound(APIClientError):
    '''raise this when there is a 404'''

class ResourceConflict(APIClientError):
    '''raise this when there is a 409'''

class ValidationError(APIClientError):
    '''raise this when there is a 422'''
