"""File for exceptions classes"""

BASE_TOKEN_ERROR_MSG = 'Api key must provided'


class GiphyTokenError(Exception):
    """Base class for token errors"""
    def __init__(self, msg=BASE_TOKEN_ERROR_MSG):  # pylint: disable=super-init-not-called
        self.msg = msg

    def __str__(self):
        return self.msg
