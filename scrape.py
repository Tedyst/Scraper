import queue
from utils.utils import linkType
import time


def worker():
    while True:
        if q.qsize() == 0:
            add()
        item = q.get()
        try:
            linkType(item)
        except:
            print("Rate-Limiting...")
            print("Wait 30 min...")
            time.sleep(1800)
            continue
        q.task_done()
        print(q.qsize(), "pages remaining")
        time.sleep(400)


q = queue.Queue()


def add():
    source = open("source.txt", "r")
    for line in source:
        q.put(line)


worker()
