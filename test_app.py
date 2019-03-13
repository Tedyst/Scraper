from utils.utils import getBigPage


def test_getPage1():
    page = getBigPage("https://stoicatedy.ovh")
    assert page is None


def test_getPage2():
    page = getBigPage("https://www.emag.ro/procesoare/p1/c")
    assert page is not None
