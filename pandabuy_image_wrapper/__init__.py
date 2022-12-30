import os
import requests

PANDABUY_AUTH_KEY = os.environ.get('PANDABAY_AUTH_KEY', None)


class APIKeyMissingError(Exception):
    pass


if PANDABUY_AUTH_KEY is None:
    raise APIKeyMissingError(
        "All methods require you to use your pandabuy auth key. See "
        "https://github.com/hiihex/pandabuy-image-wrapper README "
        "for how to retrieve an authentication token from "
        "your session storage"
    )
session = requests.Session()
session.headers = {'Authorization': f"Bearer {PANDABUY_AUTH_KEY}"}

from .api import API
