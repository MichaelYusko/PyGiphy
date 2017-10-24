# from distutils.core import setup
#
# import giphy
#
# VERSION = giphy.__version__
# AUTHOR = giphy.__author__
#
# setup_kwargs = {
#     'name': 'giphy',
#     'version': VERSION,
#     'url': 'https://github.com/MichaelYusko/PyGiphy',
#     'license': 'MIT',
#     'author': AUTHOR,
#     'author_email': 'freshjelly12@yahoo.com',
#     'description': 'Python interface for the Giphy API',
#     'packages': ['giphy'],
#     'classifiers': [
#         'Development Status :: 2 - Pre-Alpha',
#         'Environment :: Web Environment',
#         'Programming Language :: Python :: 3.5',
#         'Programming Language :: Python :: 3.6',
#         'License :: OSI Approved :: MIT License'
#     ],
#  }
#
# requirements = ['requests>=2.13.0']
# setup_kwargs['install_requires'] = requirements
#
# setup(**setup_kwargs)
#
# print(u"\n\n\t\t    "
#       "PyGiphy version {} installation succeeded.\n".format(VERSION))

from giphy.client import GiphyClient

print(GiphyClient('e4bcf0c50d5e45a79ed8a8d5503a065c').translate.gifs('homer simpson'))
