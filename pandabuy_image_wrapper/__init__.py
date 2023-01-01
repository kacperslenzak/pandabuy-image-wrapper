import os
import requests

PANDABUY_AUTH_KEY = os.environ.get('PANDABUY_AUTH_KEY', None)
USER_ID = os.environ.get('PANDABUY_USER_ID', None)


class APIKeyMissingError(Exception):
    pass


class UserIDMissingError(Exception):
    pass


class InvalidURLError(Exception):
    pass


if PANDABUY_AUTH_KEY is None:
    raise APIKeyMissingError(
        "All methods require you to use your pandabuy auth key. See "
        "https://github.com/hiihex/pandabuy-image-wrapper README "
        "for how to retrieve an authentication token from "
        "your session storage"
    )


if USER_ID is None:
    raise UserIDMissingError(
        "Image retrieving methods require you to use your pandabuy User ID. See "
        "https://github.com/hiihex/pandabuy-image-wrapper README "
        "for how to retrieve your User ID from "
        "your session storage"
    )


session = requests.Session()
session.headers = {'Authorization': f'Bearer {PANDABUY_AUTH_KEY}',
                   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
session.params = {'userId': USER_ID}

from .api import API
