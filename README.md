# PyGiphy

Python3+ interface for the Giphy API

[![Build Status](https://travis-ci.org/MichaelYusko/PyGiphy.svg?branch=master)](https://travis-ci.org/MichaelYusko/PyGiphy)


Releases
=================================
* 0.1.0 - PyPi


Installation
=================================
```
pip install pygiphy
```

Usage
=================================

### Auth
```python
from giphy.client import GiphyClient

# Create an instance of GiphyClient
giphy = GiphyClient('YOUR_API_KEY')
```

### Search
```python
# Return an object with an array
# {'data': [{'type': 'gif', 'id': 'I7p8K5EY9w9dC', 'slug': 'futbol-I7p8K5EY9w9dC', ...]}
giphy.search.gifs('homer simpson')

# Add only_urls flag, in order to get urls only
# ['https://giphy.com/gifs/futbol-I7p8K5EY9w9dC', ...]
giphy.search.gifs('homer simpson', only_urls=True)

# Return an object with information
# {'data': {'type': 'gif', 'id': 'I7p8K5EY9w9dC', ...}
giphy.search.gif_by_id('I7p8K5EY9w9dC')
```

### Trending
```python
# Return an object with an array
# {'data': [{'type': 'gif', 'id': 'l378jZTJ9NenqAYLe', ...}
giphy.trending.search_gifs()

# Add only_urls flag, in order to get urls only
# ['https://giphy.com/gifs/denofthieves-den-of-thieves-l378jZTJ9NenqAYLe', ...]
giphy.trending.search_gifs(only_urls=True)
```


### Translate
```python
# Return an object with information
# {'data': {'type': 'gif', 'id': 'xU9TT471DTGJq', ...}
giphy.translate.gifs('homer simpson')
```

### Stickers
```python
# Return an object with an array
# {'data': [{'type': 'gif', 'id': 'ssm0SSwVbICGc', ...}]
giphy.stickers.get('darth vader')

# Return an object with an array
# {'data': [{'type': 'gif', 'id': '3o7aCVfbgpyPFwnc7S', ...}]
giphy.stickers.trending()

# Add only_urls flag, in order to get urls only
# ['https://giphy.com/gifs/funny-lol-3o7aCVfbgpyPFwnc7S', ... ]
giphy.stickers.trending(only_urls=True)

# Return an object
# {'data': {'type': 'gif', 'id': 'yJKAJBedeZoCk', ...}
giphy.stickers.translate('cosmic gate')

# Return an object
# {'data': {'type': 'gif', 'id': 'nAT8bBgbDmeJ2', ...}
giphy.stickers.random()
```

### Stickers Packs
```python
# Return an object with an array
# {'data': [{'id': 4788704, 'display_name': 'Accessories', ...}]
giphy.stickers_packs.listing()
```


Contribution
=================================
1. Fork the repo
2. Feel free to make a PR;)