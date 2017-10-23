"""File for the Giphy client"""
import requests

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
            _switch_paras Change params dictionary
            _get_only_url Retrieve an array with gif objects, and return with urls only
    """
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.params = {'api_key': self.api_key}

        if not api_key:
            raise GiphyTokenError

    def _switch_params(self, switch=False, query=None, **kwargs):
        """
        :param switch: Boolean argument, add arguments, or not
        :param query: Query argument for endpoints
        :param kwargs: Other keys
        :return: An dict object, with data
        """
        if switch:
            self.params['q'] = query
            self.params.update(**kwargs)
        return self.params

    def _get_only_url(self, obj):  # pylint: disable=no-self-use
        """
        :param obj: An object, with collection of gif objects.
        :return: The array with gif urls.
        """
        gifs = []
        for gif in obj['data']:
            gifs.append(gif['url'])
        return gifs

    def get(self, endpoint: str, params, **kwargs):  # pylint: disable=no-self-use
        """
        :param endpoint: An endpoint, for which we need to do a request
        :param kwargs: Other keys
        :param params: The dict object, with parameters
        :return: an dictionary with information
        """
        return requests.get(API_URL + endpoint, params=params, **kwargs).json()


class Search(BaseGiphy):
    """Class for the search endpoints
        Init:
            api_key api_key An API KEY from the Giphy service.
        Methods:
            gifs Return an array with gif object or with urls only
    """

    def __init__(self, api_key):
        super().__init__(api_key=api_key)

    def gifs(self, query: str, only_urls: bool = False, **kwargs):
        """
        :param query: An query argument
        :param only_urls: Return an array with gif urls, if True
        :param kwargs: Other keys, all available
        limit/offset/rating/lang/fmt
        :return: An dict object, with data
        """
        params = self._switch_params(True, query, **kwargs)
        response = self.get('search', params)
        if only_urls:
            response = self._get_only_url(response)
        return response


class Trending(BaseGiphy):
    """Class for the trending endpoints
        Init:
            api_key An API KEY from the Giphy service.
        Methods:
            search_gifs Return an gif objects, or urls only
    """

    def __init__(self, api_key):
        super().__init__(api_key)

    def search_gifs(self, only_urls: bool = False, **kwargs):
        """
        :param only_urls: Return an array with gif urls, if True
        :param kwargs: Other keys
        :return: return an array with objects, or with urls only
        """
        params = self._switch_params(True, **kwargs)
        response = self.get('trending', params)
        if only_urls:
            response = self._get_only_url(response)
        return response


class GiphyClient:  # pylint: disable=too-few-public-methods
    """The main client class"""
    def __init__(self, api_key):
        self.search = Search(api_key)
        self.trending = Trending(api_key)
