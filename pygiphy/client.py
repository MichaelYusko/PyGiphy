"""File for the Giphy client"""
import requests

from . import constants
from .exceptions import GiphyTokenError

API_URL = constants.API_URL_V1
STICKERS_URL = constants.API_STICKERS_URL_V1
STICKERS_PACKS_URL = constants.API_STICKERS_PACKS_URL_V1


class BaseGiphy:  # pylint: disable=too-few-public-methods
    """Base class for the each endpoint classes

        Init:
            api_key An API KEY from the Giphy service

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

    def _get(self, endpoint, params,
             stickers: bool = False,
             stickers_packs: bool = False,
             **kwargs):  # pylint: disable=no-self-use
        """
        :param endpoint: An endpoint, for which we need to do a request
        :param kwargs: Other keys
        :param params: The dict object, with parameters
        :return: an dictionary with information
        """
        base_url = API_URL

        if isinstance(endpoint, int):
            endpoint = str(endpoint)

        if stickers:
            base_url = STICKERS_URL

        if stickers_packs:
            base_url = STICKERS_PACKS_URL

        return requests.get(base_url + endpoint, params=params, **kwargs).json()


class Search(BaseGiphy):
    """Class for the search endpoints
        Init:
            api_key An API KEY from the Giphy service.
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
        response = self._get('search', params)
        if only_urls:
            response = self._get_only_url(response)
        return response

    def gif_by_id(self, gif_id: str):
        """
        :param gif_id: An id of gif
        :return: An dict with gif object
        """
        return self._get(gif_id, self.params)


class Trending(BaseGiphy):  # pylint: disable=too-few-public-methods
    """Class for the trending endpoints
        Init:
            api_key An API KEY from the Giphy service.
        Methods:
            search_gifs Return an gif objects, or urls only
    """

    def __init__(self, api_key):  # pylint: disable=useless-super-delegation
        super().__init__(api_key)

    def search_gifs(self, only_urls: bool = False, **kwargs):
        """
        :param only_urls: Return an array with gif urls, if True
        :param kwargs: Other keys
        :return: return an array with objects, or with urls only
        """
        params = self._switch_params(True, **kwargs)
        response = self._get('trending', params)
        if only_urls:
            response = self._get_only_url(response)
        return response


class Translate(BaseGiphy):
    """Class for the translate endpoints
        Init:
            api_key An API KEY from the Giphy service.

        Methods:
            gifs Return an dict, by string argument
    """
    def __init__(self, api_key):  # pylint: disable=useless-super-delegation
        super().__init__(api_key)

    def gifs(self, s: str):
        """
        :param s: An string, for example 'ryan gosling'
        :return: An dict object with information
        """
        self.params['s'] = s
        response = self._get('translate', self.params)
        return response


class Stickers(BaseGiphy):
    """Class for the stickers endpoints
        Init:
            api_key An API KEY from the Giphy service

        Methods:
            get Return an array with stickers
    """

    def __init__(self, api_key):
        super().__init__(api_key)

    def get(self, query: str, **kwargs):
        """
        :param query: An query argument
        :param kwargs: Other keys, all available
        limit/offset/rating/lang/fmt
        :return:
        """
        params = self._switch_params(True, query, **kwargs)
        response = self._get('search', params, stickers=True, **kwargs)
        return response

    def trending(self, only_urls: bool = False, **kwargs):
        """
        :param only_urls: Return urls only
        :param kwargs: Other keys, all available
        fmt/limit/rating
        :return: And anrray with sticker objects
        """
        params = self._switch_params(True, **kwargs)
        response = self._get('trending', params, stickers=True, **kwargs)
        if only_urls:
            response = self._get_only_url(response)
        return response

    def translate(self, s: str):
        """
        :param s: An string argument
        :return: An object with stickers
        """
        self.params['s'] = s
        response = self._get('translate', self.params, True)
        return response

    def random(self, **kwargs):
        """
        :param kwargs: Other keys, all available
        tag/rating/fmt
        :return:
        """
        response = self._get('random', self.params, stickers=True, **kwargs)
        return response


class StickerPacks(BaseGiphy):
    """Class for the sticker packs endpoints
        Init:
            api_key  An API KEY from the Giphy service.
        Methods:
            listing Returns a list of all sticker packs available.
                    Hand-curated by the GIPHY editorial team.
    """
    def __init__(self, api_key):
        super().__init__(api_key)

    def listing(self):
        """
        :return: An array with objects
        """
        response = self._get('packs', self.params, stickers=True)
        return response


class GiphyClient:
    """The main client class"""
    def __init__(self, api_key):
        self._key = api_key
        self.search = Search(api_key)
        self.trending = Trending(api_key)
        self.translate = Translate(api_key)
        self.stickers = Stickers(api_key)
        self.stickers_packs = StickerPacks(api_key)

    def __repr__(self):
        return "GiphyClient(API_KEY={})".format(self._key)
