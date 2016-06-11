from gevent import monkey
monkey.patch_all()

import time
import requests
import gevent.pool
import gevent.queue
import gevent

session = requests.Session()
max_workers = 32
pool = gevent.pool.Pool(max_workers)
queue = gevent.queue.Queue()

pool.start(pool.spawn(a,'none'))
pool.join()


while not queue.empty() and not pool.full():
    for x in xrange(0, min(queue.qsize(), pool.free_count())):
        t = queue.get_nowait()
        pool.start(pool.spawn(t[0],t[1]))
pool.join()
