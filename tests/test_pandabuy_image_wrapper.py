from pandabuy_image_wrapper import API
from pytest import fixture
import os


@fixture
def reference_image_keys():
    """
    Responsible only for returning the test data
    :return:
    """
    return ['url', 'imageList']


def test_reference_images(reference_image_keys):
    """
    Tests an API Call to get a products refernce images
    :return:
    """

    instance = API(auth_token=os.environ.get('PANDABUY_AUTH_KEY', None))
    response = instance.get_images(url="https://weidian.com/item.html?itemID=4450402251&spider_token=4572")

    assert isinstance(response, dict)
    assert response['url'] == "https://weidian.com/item.html?itemID=4450402251&spider_token=4572"
    assert set(reference_image_keys).issubset(response.keys())
