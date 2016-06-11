import requests
import json
import pprint

#List of Hashtags
hashtags=['RailaInNakuru',
'AUSvENG',
'KCBSafariRally',
'MsetoExtra',
'GiladOnClub999Degrees',
'Panama',
'Giroud',
'Payet',
'Burundi',
'Monday+and+Thursday',
'BREAKING+NEWS',
'Chase+Bank',
'Governor+Nderitu+Gachagua',
'CS+Joseph+Nkaissery',
'Kidero',
'Nigeria',
'Wenger',
'Auditor+General',
'Ramadan',
'QwetuRoadShow',
'TourismLiveKE',
'SiganaFest2016',
'EURO2016',
'UhuruInUkambani',
'QTVJAMROCK',
'NBAFinals',
'FaithFriday',
'TwendeMacha',
'WBWR',
'MuhammadAli',
'NZLvWAL',
'TransformingCounties',
'HOTSMS',
'EbruNewsUpdate',
'AlbinismKE']

#The parent array which consists of all the data extracted from various Social Media Platforms
all_social_media_link=[]

#Creating pprint object
pp = pprint.PrettyPrinter(indent=4)

#Function which pulls the data 
def data_social_medias(hashtag):

	r=requests.get("https://post-cache.tagboard.com/search/"+hashtag+"?excluded_networks=twitter&count=100")

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
		except:
			pass

		all_social_media_link.append(social_media_dictionary)


for hashtag in hashtags:
	data_social_medias(hashtag)

pp.pprint(all_social_media_link)	
print len(all_social_media_link)


