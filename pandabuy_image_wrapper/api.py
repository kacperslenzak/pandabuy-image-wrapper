class API(object):
    def __init__(self, auth_token):
        self.auth_token = auth_token

    def get_images(self, url):
        return {'url': url}
