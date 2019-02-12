import queue
from functii import linkType
import time


def worker():
    while True:
        if q.qsize() == 0:
            add()
        item = q.get()
        try:
            linkType(item)
        except:
            print("eMag a dat rate-limiting...")
            print("Wait 30 min...")
            time.sleep(1800)
            continue
        q.task_done()
        print(q.qsize(), "pagini ramase")
        time.sleep(120)


q = queue.Queue()


def add():
    source = open("source.txt", "r")
    for line in source:
        q.put(line)


worker()
