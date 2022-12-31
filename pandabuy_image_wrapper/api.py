from . import session


class API(object):
    def __init__(self, auth_token):
        self.auth_token = auth_token

    @staticmethod
    def get_images(url) -> dict:
        path = "https://www.pandabuy.com/gateway/order/itemGet?url={}".format(url)
        response = session.get(path).json()

        if response.get('timeInfo'):
            image_list = response['data']['item']['timeInfo']['imageList']
        else:
            image_list = []

        output = {
            'url': url,
            'imageList': image_list
        }

        return output
