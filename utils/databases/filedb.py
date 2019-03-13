import pickle


def log(data):
    res = []
    try:
        f = open("db.txt", "rb")
        res = pickle.load(f)
    except:
        print("db.txt not found")
    res.extend([data])
    print(res)
    f2 = open("db.txt", "wb")
    pickle.dump(res, f2)
    f2.flush()


def read():
    f = open("db.txt", "rb")
    return pickle.load(f)
