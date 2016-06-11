from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import pprint
import json

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

# CONSUMER_KEY = "rcPzx7rJtywQMk0VmdGLCAxjb"
# CONSUMER_SECRET = "DE3J8NLlSVSnGJuQ0U3GKCBjrIo7vBxQCEeCOj1HoS2bP74NPv"

# CONSUMER_KEY = "N8CefcBhNEgLLzj5C5NTkwk7I"
# CONSUMER_SECRET = "XvalzhATRiMwtRmz5g6jrU4yI9VrMvGRbPYpWaXYtPEofMYyMT"

# CONSUMER_KEY="XX254OwNWCuctNrlo29GW2Ihx"
# CONSUMER_SECRET = "KDTb6Q4swNH1ThMO13SH9vzhOQecP9705wFXw6qPg90S52ISZU"

CONSUMER_KEY="gcLU6rXGwRHUaWOSl9J648bkp"
CONSUMER_SECRET = "JQ5E8Wn0XutYqslBdjGRJxi5snbh2bDmGAeq3mI8bXnmyYVVAn"




# OAUTH_TOKEN = "4653955494-jbxlbxolDzQv16TA6astzszHOT7HHJbtZTy5HNV"
# OAUTH_TOKEN_SECRET = "3ndOvcdpb79OR73BfJtJ64i9Qg6X8qWIpcI4SAcnIfKSB"

# OAUTH_TOKEN ="4653955494-Cbul45ZQvzsK16aELSN2O6ecVaT4UbSDujfCkqx"
# OAUTH_TOKEN_SECRET = "8CwjuAi7ctdJQIfW4a835IdLYcap8cl5V2ZPaG0rm7exW"

# OAUTH_TOKEN="4653955494-VRs3MN2aPRhiQFBIdPyMs8S68X1cxaBT81s0bY7"
# OAUTH_TOKEN_SECRET="2eAn9kfBofZpuFHuYaakbwbNqrpeesInMas1AAdkxQKb1"

OAUTH_TOKEN= "4653955494-2z4klWrjEk8PhV1HCT9QFvibjPouDuj0z2YIQh6"
OAUTH_TOKEN_SECRET="Kb01dB5abJyhW7to5rYRB9CTW0LwDwG6F4mOUMEQlTxYw"




coun = ["Afghanistan","Argentina","Armenia","Australia","Austria","Bahrain","Canada","Central African Republic","Chad","Chile","China","Colombia","Comoros","Congo","Costa Rica","Croatia","Cuba","Cyprus","Czech Republic","North Korea","Democratic Republic of the Cong","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Ethiopia","Fiji","Finland","France","Gabon","Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","Kuwait","Kyrgyzstan","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia","Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar","Namibia","Nauru","Nepal","Netherlands","New Zealand","Nicaragua","Niger","Nigeria","Norway","Oman","Pakistan","Palau","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Republic of Korea (South Korea)","Republic of Moldova","Romania","Russian Federation","Rwanda","Saint Kitts and Nevis","Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Sudan","Spain","Sri Lanka","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syrian Arab Republic","Tajikistan","Thailand","Timor-Leste","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom of Great Britain and Northern Ireland","United Republic of Tanzania","United States of America","Uruguay","Uzbekistan","Vanuatu","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe"]

woeid = [u'23424740', u'23424747', u'23424748', u'23424750', u'23424775', u'23424782', u'23424787', u'23424868', u'23424796', u'23424800', u'23424801', u'23424802', u'23424819', u'23424829', u'23424824', u'23424833', u'83123', u'23424848', u'23424846', u'23424803', u'23424852', u'23424853', u'23424858', u'23424856', u'2429994', u'23424874', u'23424899', u'23424891', u'23424897', u'23424932', u'23424896', u'23424894', u'23424900', u'24865720', u'483301', u'23424887', u'20069817', u'23424893', u'23424902', u'23424763', u'23424987', u'23424912', u'23424911', u'23424909', u'23424916', u'23424906', u'23424908', u'29145317', u'23424898', u'23424922', u'23424927', u'159386', u'12491802', u'23424917', u'23424919', u'23424934', u'23424923', u'23424925', u'28395013', u'23424868', u'23424885', u'23424933', u'23424936', u'23424937', u'23424940', u'1325621', u'2347676', u'23424992', u'532373', u'1441680', u'29125356', u'23424943', u'20069818', u'23424941', u'1062844', u'1062617', u'23424877', u'23424945', u'23424766', u'23424949', u'24865670', u'23424952', u'23424950', u'12467072', u'905958', u'23424913', u'23424993', u'23424954', u'23424957', u'23424956', u'23424961', u'23424960', u'23424968', u'1048627', u'23424964', u'23424958', u'23424967', u'23424969', u'23424972', u'23424970', u'1301134', u'23424976', u'23424738', u'20070563', u'23424973', u'23424977', u'23424979', u'23424980', u'23424907', u'23424982', u'23424984', u'23425002', u'23425003', u'23425004']





def setup_oauth():
    """Authorize your app via identifier."""
    # Request token
    oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)

    resource_owner_key = credentials.get('oauth_token')[0]
    resource_owner_secret = credentials.get('oauth_token_secret')[0]

    # Authorize
    authorize_url = AUTHORIZE_URL + resource_owner_key
    print 'Please go here and authorize: ' + authorize_url

    verifier = raw_input('Please input the verifier: ')
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)

    # Finally, Obtain the Access Token
    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    token = credentials.get('oauth_token')[0]
    secret = credentials.get('oauth_token_secret')[0]

    return token, secret

pp = pprint.PrettyPrinter(indent=4)

def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

dic = {}
def get_trend_hashtags(woeid):
        for i in woeid[25:]:
            # try:
            b = requests.get(url="https://api.twitter.com/1.1/trends/place.json?id="+i+"", auth=oauth)
            # print b.json()
            tag =[]
            try:

                for j in b.json()[0]['trends']:
                    print j["query"]
            except Exception as e:
                woeid.remove(i)
                print i
                print woeid
                print b.json()

            # for i in b.json()[0]:
            #     tag.append(i['trends']["query"])
            # dic[i] = tag
            # print dic
            # except:
            #     print "not available"









if __name__ == "__main__":
    if not OAUTH_TOKEN:
        token, secret = setup_oauth()
        print "OAUTH_TOKEN: " + token
        print "OAUTH_TOKEN_SECRET: " + secret
        print
    else:
        oauth = get_oauth()
        get_trend_hashtags(woeid)
        # r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=messi&count=100", auth=oauth)
        # a = r.json()
        # print len(a)
        # for i in range(0,100):
        #
        #     print "tweet="+a['statuses'][i]['text']
        #     print "place="+str(a['statuses'][i]['place'])
        #     print "coordibnates="+str(a['statuses'][i]['coordinates'])
            # print a['statuses'][0]['text']
            # print "tweet="+a['statuses'][1]['text']
            # print "place="+a['statuses'][1]['place']
        # pp.pprint(r.json())
