from . import session


class API(object):
    def __init__(self, auth_token):
        self.auth_token = auth_token

    @staticmethod
    def get_images(url):
        path = "https://www.pandabuy.com/gateway/order/itemGet?url={}".format(url)
        response = session.get(path).json()

        print(response)

        output = {
            'url': url,
            'imageList': response['data']['item']['timeInfo']['imageList']
        }

        return output
