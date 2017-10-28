"""File for tests"""
import json
import unittest

from mock import MagicMock, patch

from pygiphy.client import GiphyClient

json_data = [{
    'id': '1',
    'name': 'Monkey'
}]

mock_data = MagicMock(status_code=200, json_data=json_data)


class TestGiphy(unittest.TestCase):
    """Test class for the Giphy client class"""

    def setUp(self):
        self.client = GiphyClient('API_KEY')
        self.json_data = json.dumps(json_data)
        self.mock_data = mock_data

    def tearDown(self):
        pass

    def return_assert(self, request, func):
        request.get.return_value = ['31231', '31312']
        return self.assertTrue(self.json_data, func)

    @patch('pygiphy.client.requests')
    def test_search_gifs(self, request):
        self.return_assert(request, self.client.search.gifs(query='Batman'))

    @patch('pygiphy.client.requests')
    def test_only_urls(self, request):
        self.return_assert(request, self.client.search.gifs(query='Batman',
                                                            only_urls=True))

    @patch('pygiphy.client.requests')
    def test_gif_by_id(self, request):
        self.return_assert(request, self.client.search.gif_by_id('132131'))

    @patch('pygiphy.client.requests')
    def test_trending_search_gifs(self, request):
        self.return_assert(request, self.client.trending.search_gifs(query='Batman'))

    @patch('pygiphy.client.requests')
    def test_trending_search_gifs_ony(self, request):
        self.return_assert(request, self.client.trending.search_gifs(query='Batman',
                                                                     only_urls=True))

    @patch('pygiphy.client.requests')
    def test_translate_gifs(self, request):
        self.return_assert(request, self.client.translate.gifs(s='Homer simpson'))

    @patch('pygiphy.client.requests')
    def test_stickers_get(self, request):
        self.return_assert(request, self.client.stickers.get(query='Homer simpson'))

    @patch('pygiphy.client.requests')
    def test_stickers_trending(self, request):
        self.return_assert(request, self.client.stickers.trending(query='Homer simpson'))

    @patch('pygiphy.client.requests')
    def test_stickers_trending_only_url(self, request):
        self.return_assert(request, self.client.stickers.trending(query='Homer simpson',
                                                                  only_urls=True))

    @patch('pygiphy.client.requests')
    def test_stickers_translate(self, request):
        self.return_assert(request, self.client.stickers.trending(s='Homer simpson'))

    @patch('pygiphy.client.requests')
    def test_stickers_random(self, request):
        self.return_assert(request, self.client.stickers.random())

    @patch('pygiphy.client.requests')
    def test_stickers_packs_listing(self, request):
        self.return_assert(request, self.client.stickers_packs.listing())


if __name__ == '__main__':
    unittest.main()
