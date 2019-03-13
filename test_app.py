from utils.utils import getPage


def test_getPage1():
    page = getPage("https://stoicatedy.ovh")
    assert page is None


def test_getPage2():
    page = getPage("https://www.emag.ro/procesoare/p1/c")
    assert page is not None
