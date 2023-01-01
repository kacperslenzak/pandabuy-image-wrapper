from re import sub
from pandabuy_image_wrapper import InvalidURLError


def validate_url(url) -> bool:
    pattern = "http(s)?(:)?(\/\/)?|(\/\/)?(www\.)?"
    url_stripped_protocol = sub(pattern, "", url)
    allowed_urls = (
        "item.taobao.com",
        "detail.tmall.com",
        "weidan.com",
        "detail.1688.com"
    )

    if not url_stripped_protocol.startswith(allowed_urls):
        return False

    return True


