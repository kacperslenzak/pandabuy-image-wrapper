from pandabuy_image_wrapper import API


def test_reference_images():
    """
    Tests an API Call to get a products refernce images
    :return:
    """

    instance = API(authorization_token="TOKEN")
    response = instance.get_images(url="https://weidian.com/item.html?itemID=4450402251&spider_token=4572")

    assert isinstance(response, dict)
    assert response['url'] == "https://weidian.com/item.html?itemID=4450402251&spider_token=4572"