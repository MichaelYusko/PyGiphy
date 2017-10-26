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
        request.get.return_value = self.mock_data
        return self.assertTrue(self.json_data, func)

    @patch('pygiphy.client.requests')
    def test_search_gifs(self, request):
        self.return_assert(request, self.client.search.gifs(query='Batman'))


if __name__ == '__main__':
    unittest.main()
