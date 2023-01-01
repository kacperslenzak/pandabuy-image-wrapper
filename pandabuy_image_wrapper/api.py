from pandabuy_image_wrapper import session, InvalidURLError, TokenInvalidationError
from pandabuy_image_wrapper.helpers import validate_url


class API(object):
    def __init__(self, auth_token):
        self.auth_token = auth_token

    @staticmethod
    def get_images(url) -> dict:
        if not validate_url(url):
            raise InvalidURLError(
                "You passed an invalid URL. See "
                "https://github.com/hiihex/pandabuy-image-wrapper README "
                "on what urls are allowed to be passed "
                "to fetch Images"
            )

        path = "https://www.pandabuy.com/gateway/order/itemGet?url={}".format(url)
        response = session.get(path).json()

        if response.get("code") and response['code'] != 200:
            if response['code'] == 10010:
                raise TokenInvalidationError(
                    "Token or User ID is invalid. See "
                    "https://github.com/hiihex/pandabuy-image-wrapper README "
                    "to check how to fetch and set your "
                    "Auth Token and User ID. "
                )
            else:
                raise BaseException(
                    "Unknown Error"
                )

        if response.get('timeInfo'):
            image_list = response['data']['item']['timeInfo']['imageList']
        else:
            image_list = []

        output = {
            'url': url,
            'imageList': image_list
        }

        return output
