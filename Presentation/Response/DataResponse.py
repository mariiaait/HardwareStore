class DataResponse:
    def __init__(self, is_success, response, errors):
        self._is_success = is_success
        self._response = response
        self._errors = errors

    @property
    def is_success(self):
        return self._is_success
    @is_success.setter
    def is_success(self, value):
        self._is_success = value
    @property
    def response(self):
        return self._response
    @response.setter
    def response(self, value):
        self._response = value
    @property
    def errors(self):
        return self._errors
    @errors.setter
    def errors(self, value):
        self._errors = value