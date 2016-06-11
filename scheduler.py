from gevent import monkey
monkey.patch_all()

import time
import requests
import gevent.pool
import gevent.queue
import gevent
import json
import data as data

session = requests.Session()
max_workers = 32
pool = gevent.pool.Pool(max_workers)
queue = gevent.queue.Queue()

hashtags=['RailaInNakuru','AUSvENG','KCBSafariRally','MsetoExtra','GiladOnClub999Degrees',
'Panama','Giroud','Payet','Burundi','Monday+and+Thursday','BREAKING+NEWS','Chase+Bank','Governor+Nderitu+Gachagua','CS+Joseph+Nkaissery','Kidero','Nigeria','Wenger','Auditor+General','Ramadan','QwetuRoadShow','TourismLiveKE','SiganaFest2016','EURO2016','UhuruInUkambani','QTVJAMROCK','NBAFinals','FaithFriday','TwendeMacha','WBWR','MuhammadAli','NZLvWAL','TransformingCounties','HOTSMS',
'EbruNewsUpdate','AlbinismKE']

def data_social_medias(hashtag):
    print 'Requesting hashtag - ',hashtag
    r=session.get("https://post-cache.tagboard.com/search/"+hashtag+"?count=100")

    social_media_data=json.loads(r.text)
    no_of_posts=len(social_media_data['posts'])

    for i in range(0,no_of_posts):
    	social_media_dictionary={}
    	try:
            social_media_dictionary['text']=social_media_data['posts'][i]['text'].encode('ascii', errors='ignore')
            social_media_dictionary['social_media_network']=social_media_data['posts'][i]['network']
            social_media_dictionary['social_media_link']=social_media_data['posts'][i]['permalink']
            social_media_dictionary['user_profile_image']=social_media_data['posts'][i]['user_profile_image_url'].replace("//","")
            social_media_dictionary['time']=social_media_data['posts'][i]['post_time']
            social_media_dictionary['post_date']=social_media_data['posts'][i]['post_date'][:-5]
            social_media_dictionary['real_user_name']=social_media_data['posts'][i]['user_real_name'].encode('ascii', errors='ignore')
            social_media_dictionary['photos']=social_media_data['posts'][i]['photos'].replace("//","")
            social_media_dictionary['videos']=social_media_data['posts'][i]['videos']
            social_media_dictionary['post_id']=social_media_data['id']
        except:
            pass
        data.all_social_media_link.append(social_media_dictionary)
        # data.all_social_media_link += str(social_media_dictionary)
    print 'Recieved hashtag - ',hashtag



def main():
    for item in hashtags:
        pool.start(pool.spawn(data_social_medias,item))
    pool.join()


    while not queue.empty() and not pool.full():
        for x in xrange(0, min(queue.qsize(), pool.free_count())):
            t = queue.get_nowait()
            pool.start(pool.spawn(t[0],t[1]))
    pool.join()
