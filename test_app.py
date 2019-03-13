def test_getPage1():
    from utils.utils import getBigPage
    page = getBigPage("https://stoicatedy.ovh")
    assert page is None


def test_getPage2():
    from utils.utils import getBigPage
    page = getBigPage("https://www.emag.ro/procesoare/p1/c")
    assert page is not None


def test_filedb():
    import os
    from utils.databases.filedb import log
    import pickle
    try:
        os.remove("db.txt")
    except:
        pass
    data = [1, 1, 'asd', 'https://stoicatedy.ovh', 'emag']
    log(data)
    f = open("db.txt", "rb")
    db = pickle.load(f)
    os.remove("db.txt")
    assert db == data


def test_filedbRead():
    import os
    from utils.databases.filedb import log, read
    try:
        os.remove("db.txt")
    except:
        pass
    data = [1, 1, 'asd', 'https://stoicatedy.ovh', 'emag']
    log(data)
    db = read()
    assert db == data
