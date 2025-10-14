
class ResourceConflict(Exception):
    '''raise this when there is a 409'''
    def __init__(self, response):
        self.status_code = response.status_code
        self.detail = response.text

class ValidationError(Exception):
    '''raise this when there is a 422'''
    def __init__(self, response):
        self.status_code = response.status_code
        self.detail = response.text

class ResourceNotFound(Exception):
    '''raise this when there is a 404'''
    def __init__(self, response):
        self.status_code = response.status_code
        self.detail = response.text