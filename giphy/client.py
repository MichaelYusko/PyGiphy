"""File for the Giphy client"""
import requests as r

from . import constants
from .exceptions import GiphyTokenError

API_URL = constants.API_URL_V1
STICKERS_URL = constants.API_STICKERS_URL_V1


class BaseGiphy:  # pylint: disable=too-few-public-methods
    """Base class for the each endpoint classes

        Init:
            api_key An API KEY from the Giphy service.

        Methods:
            get Make an get request, with default parameters
    """
    def __init__(self, api_key):
        self.api_key = api_key
        self.params = {'api_key': self.api_key}

        if not api_key:
            raise GiphyTokenError

    def get(self, endpoint: str, **kwargs):
        """
        :param endpoint: An endpoint, for which we need to do a request
        :param kwargs: Other keys
        :return: an dictionary with information
        """
        return r.get(API_URL + endpoint, params=self.params, **kwargs).json()


class Search(BaseGiphy):  # pylint: disable=too-few-public-methods
    """class for the search endpoints"""
    pass
