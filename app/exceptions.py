from http import HTTPStatus


class ResponseException(Exception):

    status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    reason = "intervalServerError"
    phrase = "Internal server error"

    def __init__(self, status_code: HTTPStatus = None, reason: str = None, phrase: str = None):

        if status_code is not None:
            self.status_code = status_code

        if reason is not None:
            self.reason = reason
        elif status_code is not None:
            self.reason = status_code.phrase

        if phrase is not None:
            self.phrase = phrase
        elif status_code is not None:
            self.phrase = status_code.description

        super().__init__(self.phrase)
