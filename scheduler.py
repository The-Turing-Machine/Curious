
from gevent import monkey
monkey.patch_all()

import datetime
import requests
import gevent.pool
import gevent.queue
import gevent
import json
import data as data
import twitter as twitter

session = requests.Session()
max_workers = 32
req = 0
pool = gevent.pool.Pool(max_workers)
queue = gevent.queue.Queue()

# hashtags=['RailaInNakuru','AUSvENG','KCBSafariRally','MsetoExtra','GiladOnClub999Degrees','Panama','Giroud','Payet','Burundi','Monday+and+Thursday','BREAKING+NEWS','Chase+Bank','Governor+Nderitu+Gachagua','CS+Joseph+Nkaissery','Kidero','Nigeria','Wenger','Auditor+General','Ramadan','QwetuRoadShow','TourismLiveKE','SiganaFest2016','EURO2016','UhuruInUkambani','QTVJAMROCK','NBAFinals','FaithFriday','TwendeMacha','WBWR','MuhammadAli','NZLvWAL','TransformingCounties','HOTSMS','EbruNewsUpdate','AlbinismKE']

def LanguageIdentification(text_query_full):
    global req
    print 'Request sent for ', text_query_full['post_id']
    pid = text_query_full['post_id']
    text_query = text_query_full['text']
    try:

        language_dictionary={}
        r1=requests.get("https://api.havenondemand.com/1/api/sync/identifylanguage/v1?apikey=22469062-d90b-45bd-94c7-1399b139ba8f&text="+text_query)
        req+=1
        api_response=json.loads(r1.text)
        detected_language=api_response['language']
        language_dictionary[pid]=detected_language
        data.all_detected_languages.append(language_dictionary)
    except:
        pass
    print 'Request recieved for ', pid, language_dictionary

def data_social_medias(hashtag):
    global req
    print 'Requesting hashtag - ',hashtag
    r=session.get("https://post-cache.tagboard.com/search/"+hashtag+"?count=100")
    req+=1
    social_media_data=json.loads(r.text)
    no_of_posts=len(social_media_data['posts'])

    for i in range(0,no_of_posts):
    	social_media_dictionary={}
        social_media_dictionary['hashtag'] = hashtag
        social_media_dictionary['post_id']=social_media_data['posts'][i]['post_id']

        if 'videos' in social_media_data['posts'][i]:
            try:
                l = social_media_data['posts'][i]['videos'][0]
                social_media_dictionary['videos'] = [ x.replace("//","") for x in [ l['t'],l['p'],l['s'],l['m'] ] ]
                # print social_media_dictionary['videos']
            except:
                pass
        if 'photos' in social_media_data['posts'][i]:
            try:
                l = social_media_data['posts'][i]['photos'][0]
                social_media_dictionary['photos'] = [ x.replace("//","") for x in [ l['s'],l['m'],l['l'] ] ]
            except:
                pass
    	try:

            social_media_dictionary['text']=social_media_data['posts'][i]['text'].encode('ascii', errors='ignore')
            social_media_dictionary['social_media_network']=social_media_data['posts'][i]['network']
            social_media_dictionary['social_media_link']=social_media_data['posts'][i]['permalink']
            social_media_dictionary['user_profile_image']=social_media_data['posts'][i]['user_profile_image_url'].replace("//","")
            epoch_time=social_media_data['posts'][i]['post_time']
            real_time=datetime.datetime.fromtimestamp(epoch_time).strftime("%c")
            social_media_dictionary['time']=real_time
            social_media_dictionary['post_date']=social_media_data['posts'][i]['post_date'][:-5]
            social_media_dictionary['real_user_name']=social_media_data['posts'][i]['user_real_name'].encode('ascii', errors='ignore')

        except:
            pass
        data.all_social_media_link.append(social_media_dictionary)
        queue.put_nowait((LanguageIdentification,social_media_dictionary))

    print 'Recieved hashtag - ',hashtag

def main():
    twitter.main()
    data_twitter = twitter.dic
    # data.top_tags = [ { 'country':key,'coords': data_twitter[key][0],'tags': [tag[0][3:] for tag in data_twitter[key][1:] if '%' not in tag[0][3:] ]  } for key in data_twitter.keys() ]

    data.tags_feature = [  {"type":"Feature",
                            "properties":key,
                            "geometry": {
                                    "type":"point",
                                    "coordinates":[data_twitter[key][0][1],data_twitter[key][0][0]]
                                    }
                            }  for key in data_twitter.keys() ]

    data.tags_list =  [ { 'country':key, 'tags': [tag[0][3:] for tag in data_twitter[key][1:] if '%' not in tag[0][3:] ]  } for key in data_twitter.keys() ]

    for key in data_twitter.keys():
        tags_list = [ tag[0][3:]  for tag in data_twitter[key][1:] ]
        for tag in tags_list:
            if '%' not in tag:
                queue.put_nowait((data_social_medias,tag))
    # print queue.qsize()
    #
    # for key in data.keys():
    #     print key #country
    #     print data[key][0]  #coords
    #     print data[key][1:] #list of tags

    #
    # new_dict = {}
    # new_dict['country'] =

    # for item in hashtags:
    #     queue.put_nowait((data_social_medias,item))

    while not queue.empty() and not pool.full():
        for x in xrange(0, min(queue.qsize(), pool.free_count())):
            t = queue.get_nowait()
            pool.start(pool.spawn(t[0],t[1]))
    pool.join()

# main()
# print 'No of Requests : ',req
