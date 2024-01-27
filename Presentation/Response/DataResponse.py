class DataResponse:
    def __init__(self, is_success: bool, response: str, errors: str):
        self._is_success = is_success
        self._response = response
        self._errors = errors

    @property
    def is_success(self: bool) -> bool:
        return self._is_success

    @is_success.setter
    def is_success(self, value: bool) -> None:
        self._is_success = value

    @property
    def response(self) -> dict:
        return self._response

    @response.setter
    def response(self, value: dict) -> None:
        self._response = value

    @property
    def errors(self: list) -> list:
        return self._errors

    @errors.setter
    def errors(self, value: list) -> None:
        self._errors = value

    def __getattribute__(self, name: str):
        if name in ("_is_success", "_response", "_errors"):
            raise AttributeError("Access to protected or private attributes dined")
        return object.__getattribute__(self, name)
