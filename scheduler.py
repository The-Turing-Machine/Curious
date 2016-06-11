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
req = 0
pool = gevent.pool.Pool(max_workers)
queue = gevent.queue.Queue()

hashtags=['RailaInNakuru','AUSvENG','KCBSafariRally','MsetoExtra','GiladOnClub999Degrees',
'Panama','Giroud','Payet','Burundi','Monday+and+Thursday','BREAKING+NEWS','Chase+Bank','Governor+Nderitu+Gachagua','CS+Joseph+Nkaissery','Kidero','Nigeria','Wenger','Auditor+General','Ramadan','QwetuRoadShow','TourismLiveKE','SiganaFest2016','EURO2016','UhuruInUkambani','QTVJAMROCK','NBAFinals','FaithFriday','TwendeMacha','WBWR','MuhammadAli','NZLvWAL','TransformingCounties','HOTSMS',
'EbruNewsUpdate','AlbinismKE']


def LanguageIdentification(text_query_full):
    global req
    print 'Request sent for ', text_query_full['post_id']
    pid = text_query_full['post_id']
    text_query = text_query_full['text']

    language_dictionary={}
    try:
        r1=requests.get("https://api.havenondemand.com/1/api/async/identifylanguage/v1?apikey=22469062-d90b-45bd-94c7-1399b139ba8f&text="+text_query)
        req+=1
        api_response=json.loads(r1.text)
        detected_language=api_response['actions'][0]['result']['language']
        language_dictionary[pid]=detected_language
        data.all_detected_languages.append(language_dictionary)
    except:
        pass
    print 'Request recieved for ', pid

def data_social_medias(hashtag):
    global req
    print 'Requesting hashtag - ',hashtag
    r=session.get("https://post-cache.tagboard.com/search/"+hashtag+"?count=100")
    req+=1
    social_media_data=json.loads(r.text)
    no_of_posts=len(social_media_data['posts'])

    for i in range(0,no_of_posts):
    	social_media_dictionary={}
        social_media_dictionary['post_id']=social_media_data['posts'][i]['post_id']
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

        except:
            pass
        data.all_social_media_link.append(social_media_dictionary)
        queue.put_nowait((LanguageIdentification,social_media_dictionary))
    print 'Recieved hashtag - ',hashtag

def main():
    for item in hashtags:
        queue.put_nowait((data_social_medias,item))
    # pool.join()


    while not queue.empty() and not pool.full():
        for x in xrange(0, min(queue.qsize(), pool.free_count())):
            t = queue.get_nowait()
            pool.start(pool.spawn(t[0],t[1]))
    pool.join()

main()
print 'No of Requests : ',req
