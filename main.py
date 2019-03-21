import queue
from utils.utils import linkType
import time
import utils.config as config


def worker():
    while True:
        if q.qsize() == 0:
            add()
        item = q.get()
        try:
            linkType(item)
        except AssertionError as error:
            print(error)
            print("Rate-Limiting...")
            print("Wait 300 min...")
            time.sleep(18000)
            continue
        q.task_done()
        print(q.qsize(), "pages remaining")
        time.sleep(4000)


q = queue.Queue()


def add():
    for line in config.links:
        q.put(line)


worker()
