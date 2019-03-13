import pickle


def log(data):
    try:
        f = open("db.txt", "rb")
        data.append(pickle.load(f))
    except:
        print("db.txt not found")
    f2 = open("db.txt", "wb")
    print(data)
    pickle.dump(data, f2)
    f2.flush()


def read():
    f = open("db.txt", "rb")
    return pickle.load(f)
