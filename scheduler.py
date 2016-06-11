from gevent import monkey
monkey.patch_all()

import time
import requests
import gevent.pool
import gevent.queue

def a():
    print 'func a'
    for _ in range(20):
        f = b()
        queue.put(f)

def b():
    print 'func b'
def c():
    print 'func c'

max_workers = 32
pool = gevent.pool.Pool(max_workers)
queue = gevent.queue.Queue()

def func():
    function = queue.get_nowait()
    function()


f = a()
queue.put(f)

while not queue.empty() and not pool.free_count() == max_workers:
    for x in xrange(0, min(queue.qsize(), pool.free_count())):
        pool.start(pool.spawn(func))
