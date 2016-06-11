from gevent import monkey
monkey.patch_all()

import time
import requests
import gevent.pool
import gevent.queue
import gevent

s = requests.Session()

def a(y):
    print 'func a',y
    for x in range(500):
        f = b
        queue.put((f,x))
    # print queue

def b(x):
    # gevent.sleep(2)
    r = s.get("https://post-cache.tagboard.com/search/euro2016?excluded_networks=facebook&count=100")
    print r.status_code

    print 'func b - ',x

def c():
    print 'func c'

max_workers = 32
pool = gevent.pool.Pool(max_workers)
queue = gevent.queue.Queue()

def func():
    t = queue.get_nowait()
    function = t[0]
    param = t[1]
    print param
    function(param)


f = a
# f()
# queue.put((f,'none'))
# queue.put((f,'none'))
# queue.put((f,'none'))
# queue.put((f,'none'))
pool.start(pool.spawn(a,'none'))
pool.join()


# print 'while',not queue.empty() and not pool.free_count() == max_workers
while not queue.empty() and not pool.full():
    for x in xrange(0, min(queue.qsize(), pool.free_count())):
        t = queue.get_nowait()
        print '-----'
        # print 'yo',t,pool.free_count()
        pool.start(pool.spawn(t[0],t[1]))


pool.join()
